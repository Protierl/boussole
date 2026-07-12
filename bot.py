# -*- coding: utf-8 -*-
"""
BOUSSOLE 24h/24 — bot de trading momentum en SIMULATION (capital fictif 10 000 €).
Exécuté toutes les heures par GitHub Actions : cours réels, ordres simulés,
état dans etat.json, tableau de bord dans README.md + courbe.png.
Pédagogique uniquement — aucune garantie, pas un conseil en investissement.
"""
import json, math, os, sys, time
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import requests

# ── Paramètres (identiques à l'app BOUSSOLE) ──────────────────────────
CFG = dict(capital=10000.0, topN=5, maxW=0.25, invested=0.97,
           momS=63, momL=126, sma=100, volW=20, band=0.04,
           feeRate=0.001, feeMin=1.0, minOrder=50.0,
           cooldownH=6, staleDays=4)

UNIVERSE = [
    ("AAPL","Apple","Action"), ("MSFT","Microsoft","Action"), ("NVDA","Nvidia","Action"),
    ("GOOGL","Alphabet","Action"), ("AMZN","Amazon","Action"), ("META","Meta","Action"),
    ("JPM","JPMorgan","Action"),
    ("SPY","S&P 500","ETF"), ("QQQ","Nasdaq 100","ETF"), ("EEM","Marchés émergents","ETF"),
    ("TLT","Obligations US 20 ans","ETF"), ("EZU","Zone euro","ETF"),
    ("GLD","Or","Matière première"), ("SLV","Argent","Matière première"),
    ("USO","Pétrole WTI","Matière première"), ("DBC","Panier mat. prem.","Matière première"),
]
NOM = {s:(n,c) for s,n,c in UNIVERSE}
BENCH, ETAT, DAY = "SPY", "etat.json", 86400
UA = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/125.0 Safari/537.36"}
PARIS = ZoneInfo("Europe/Paris")
now_ms = lambda: int(time.time()*1000)

# ── Formats français ──────────────────────────────────────────────────
def fnum(x, d=2):
    s = f"{x:,.{d}f}".replace(",", "\u202f").replace(".", ",")
    return s
feur = lambda x, d=2: fnum(x, d) + " €"
def fpct(x, sign=True, d=1):
    if x is None or not math.isfinite(x): return "—"
    return ("+" if sign and x > 0 else "") + fnum(x*100, d) + " %"
fdate = lambda ms: datetime.fromtimestamp(ms/1000, PARIS).strftime("%d/%m %H:%M")

# ── Données de marché : Yahoo (2 hôtes) puis Stooq en secours ─────────
def yahoo(sym, rng="1y"):
    for host in ("query1", "query2"):
        for _ in range(2):
            try:
                r = requests.get(f"https://{host}.finance.yahoo.com/v8/finance/chart/{sym}",
                                 params={"range":rng,"interval":"1d"}, headers=UA, timeout=12)
                j = r.json()["chart"]["result"][0]
                ts, cl = j["timestamp"], j["indicators"]["quote"][0]["close"]
                closes = [(int(t//DAY), round(float(c),4)) for t,c in zip(ts,cl) if c is not None]
                if len(closes) < 30: raise ValueError("série trop courte")
                m = j.get("meta", {})
                px = m.get("regularMarketPrice") or closes[-1][1]
                prev = closes[-2][1] if len(closes) > 1 else float(px)
                return {"closes":closes, "px":float(px), "prev":float(prev)}
            except Exception:
                time.sleep(0.6)
    raise RuntimeError("yahoo indisponible")

def stooq(sym):
    s = "eurusd" if sym == "EURUSD=X" else sym.lower() + ".us"
    r = requests.get(f"https://stooq.com/q/d/l/?s={s}&i=d", headers=UA, timeout=15)
    rows = [l.split(",") for l in r.text.strip().splitlines()[1:] if l.count(",") >= 4]
    closes = []
    for row in rows[-300:]:
        try:
            d = datetime.strptime(row[0], "%Y-%m-%d").replace(tzinfo=timezone.utc)
            closes.append((int(d.timestamp()//DAY), float(row[4])))
        except Exception: pass
    if len(closes) < 30: raise RuntimeError("stooq indisponible")
    return {"closes":closes, "px":closes[-1][1], "prev":closes[-2][1]}

def fetch(sym):
    try: return yahoo(sym)
    except Exception:
        try: return stooq(sym)
        except Exception: return None

# ── Indicateurs & cibles (mêmes règles que l'app) ─────────────────────
def indicateurs(closes_px):
    n = len(closes_px)
    price = closes_px[-1]
    rS = price/closes_px[-1-CFG["momS"]]-1 if n > CFG["momS"] else None
    rL = price/closes_px[-1-CFG["momL"]]-1 if n > CFG["momL"] else None
    mom = 0.5*rS+0.5*rL if (rS is not None and rL is not None) else rS
    smaV = sum(closes_px[-CFG["sma"]:])/CFG["sma"] if n >= CFG["sma"] else None
    trend = smaV is not None and price > smaV
    vol = 0.25
    if n > CFG["volW"]+1:
        rets = [closes_px[i]/closes_px[i-1]-1 for i in range(n-CFG["volW"], n)]
        m = sum(rets)/len(rets)
        vol = max(math.sqrt(sum((x-m)**2 for x in rets)/(len(rets)-1))*math.sqrt(252), 0.08)
    return dict(mom=mom, trend=trend, vol=vol,
                eligible=(mom is not None and mom > 0 and trend))

def cibles(assets):
    elig = sorted([a for a in assets if a["eligible"] and a["usable"]],
                  key=lambda a: -a["mom"])[:CFG["topN"]]
    t = {}
    if elig:
        inv = [1/a["vol"] for a in elig]; s = sum(inv)
        for a, w in zip(elig, inv):
            t[a["s"]] = min(CFG["maxW"], w/s*CFG["invested"])
    return t, {a["s"]: i+1 for i, a in enumerate(elig)}

# ── Arbitrage simulé (coût moyen, frais, ordre minimum) ───────────────
def arbitrer(etat, q, assets, fx, now):
    pos = {s: dict(p) for s, p in etat["positions"].items()}
    cash, trades = etat["cashEUR"], []
    pE = lambda s: q[s]["px"]/fx
    usable = lambda s: q.get(s, {}).get("usable")
    equity = cash + sum(p["qty"]*pE(s) for s, p in pos.items() if s in q)
    tgt, rang = cibles(assets)
    amap = {a["s"]: a for a in assets}

    def vendre(s, qty, raison):
        nonlocal cash
        px = pE(s); notion = qty*px
        fee = max(CFG["feeMin"], notion*CFG["feeRate"])
        avg = pos[s]["costEUR"]/pos[s]["qty"]
        pnl = (px-avg)*qty - fee
        cash += notion - fee
        pos[s]["qty"] -= qty; pos[s]["costEUR"] -= avg*qty
        etat["stats"]["frais"] += fee; etat["stats"]["clotures"] += 1
        if pnl > 0: etat["stats"]["gagnants"] += 1
        etat["stats"]["realise"] += pnl
        if pos[s]["qty"] <= 1e-7: pos.pop(s)
        trades.append(dict(t=now, sym=s, nom=NOM[s][0], cat=NOM[s][1], sens="VENTE",
                           qty=qty, px=q[s]["px"], fx=fx, valEUR=notion, frais=fee, pnl=pnl, raison=raison))

    def acheter(s, voulu, raison):
        nonlocal cash
        px = pE(s)
        notion = min(voulu, max(0.0, cash/(1+CFG["feeRate"]) - CFG["feeMin"]))
        if notion < CFG["minOrder"]: return
        fee = max(CFG["feeMin"], notion*CFG["feeRate"])
        if cash < notion + fee: notion = cash - fee
        if notion < CFG["minOrder"]: return
        qty = notion/px
        cash -= notion + fee
        p = pos.setdefault(s, dict(qty=0.0, costEUR=0.0))
        p["qty"] += qty; p["costEUR"] += notion + fee
        etat["stats"]["frais"] += fee
        trades.append(dict(t=now, sym=s, nom=NOM[s][0], cat=NOM[s][1], sens="ACHAT",
                           qty=qty, px=q[s]["px"], fx=fx, valEUR=notion, frais=fee, pnl=None, raison=raison))

    for s in list(pos):
        if not usable(s): continue
        w = pos[s]["qty"]*pE(s)/equity
        tw = tgt.get(s, 0.0)
        if tw == 0:
            a = amap.get(s)
            raison = ("Momentum devenu négatif" if a and a["mom"] is not None and a["mom"] <= 0
                      else "Filtre de tendance (< MM100)" if a and not a["trend"]
                      else f"Sorti du Top {CFG['topN']}")
            vendre(s, pos[s]["qty"], raison)
        elif w - tw > CFG["band"]:
            vendre(s, (w-tw)*equity/pE(s), f"Allègement vers {round(tw*100)} %")

    achats = []
    for s, tw in tgt.items():
        if not usable(s): continue
        w = pos[s]["qty"]*pE(s)/equity if s in pos else 0.0
        need = tw - w
        if need > CFG["band"] or (s not in pos and need > CFG["band"]*0.75):
            achats.append((need, s, tw, s in pos))
    for need, s, tw, deja in sorted(achats, reverse=True):
        acheter(s, need*equity,
                f"Renforcement vers {round(tw*100)} %" if deja else f"Entrée momentum · rang {rang.get(s,'–')}")
    return pos, cash, trades, tgt

# ── Statistiques de performance ───────────────────────────────────────
def perf(histo, cree, equity):
    out = dict(totalR=equity/CFG["capital"]-1, pnl=equity-CFG["capital"],
               cagr=None, maxDD=None, vol=None, sharpe=None, dayR=None)
    parjour, last_prev = {}, None
    for p in histo:
        d = datetime.fromtimestamp(p["t"]/1000, PARIS).date()
        parjour[d] = p["eq"]
    today = datetime.now(PARIS).date()
    for d in sorted(parjour):
        if d != today: last_prev = parjour[d]
    parjour[today] = equity
    daily = [parjour[d] for d in sorted(parjour)]
    jours = max((now_ms()-cree)/1000/DAY, 0.04)
    if jours >= 1: out["cagr"] = (equity/CFG["capital"])**(365/jours) - 1
    peak, dd = -1e18, 0.0
    for v in daily:
        peak = max(peak, v); dd = min(dd, v/peak-1)
    out["maxDD"] = dd
    if len(daily) >= 5:
        rets = [daily[i]/daily[i-1]-1 for i in range(1, len(daily))]
        m = sum(rets)/len(rets)
        sd = math.sqrt(sum((x-m)**2 for x in rets)/(len(rets)-1))
        out["vol"] = sd*math.sqrt(252)
        if sd > 0: out["sharpe"] = m/sd*math.sqrt(252)
    if last_prev: out["dayR"] = equity/last_prev - 1
    return out

# ── Courbe (thème sombre) ─────────────────────────────────────────────
def courbe(histo):
    if len(histo) < 2: return False
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    xs = [datetime.fromtimestamp(p["t"]/1000, PARIS) for p in histo]
    fig, ax = plt.subplots(figsize=(8, 4.1), dpi=160)
    fig.patch.set_facecolor("#0D1219"); ax.set_facecolor("#0D1219")
    b = [p.get("bench") for p in histo]
    if any(v is not None for v in b):
        ax.plot(xs, [v if v is not None else float("nan") for v in b],
                color="#8DA0B5", lw=1.1, ls="--", label="S&P 500 (10 k€)")
    ax.plot(xs, [p["eq"] for p in histo], color="#D9A441", lw=2.0, label="Bot")
    ax.fill_between(xs, [p["eq"] for p in histo], color="#D9A441", alpha=0.12)
    ax.axhline(CFG["capital"], color="#5B6B7E", lw=0.8, ls=":")
    ax.grid(color="#26303F", ls=(0,(3,5)), lw=0.6)
    for sp in ax.spines.values(): sp.set_visible(False)
    ax.tick_params(colors="#8DA0B5", labelsize=8)
    ax.yaxis.set_major_formatter(lambda v, _: f"{v/1000:.1f} k€".replace(".", ","))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m", tz=PARIS))
    leg = ax.legend(loc="upper left", frameon=False, fontsize=8)
    for t in leg.get_texts(): t.set_color("#EAF0F7")
    fig.tight_layout()
    fig.savefig("courbe.png", facecolor="#0D1219")
    plt.close(fig)
    return True

# ── Tableau de bord (README.md du dépôt) ──────────────────────────────
def rapport(etat, lignes, equity, invested, p, sig, tgt, fx, avec_courbe, mode_src):
    L = []
    m = datetime.now(PARIS).strftime("%d/%m/%Y à %H:%M")
    L.append("# 🧭 BOUSSOLE — bot 24h/24\n")
    L.append(f"**SIMULATION · cours réels · capital fictif** — mis à jour le {m} (Paris) · sources : {mode_src}\n")
    signe = "🟢" if p["pnl"] >= 0 else "🔴"
    L.append(f"## {signe} {feur(equity)}\n")
    jour = f" · jour {fpct(p['dayR'])}" if p["dayR"] is not None else ""
    L.append(f"**{'+' if p['pnl']>=0 else ''}{feur(p['pnl'])} ({fpct(p['totalR'])})**{jour} depuis le {datetime.fromtimestamp(etat['creeLe']/1000, PARIS).strftime('%d/%m/%Y')}\n")
    if avec_courbe: L.append("![Courbe de performance](courbe.png)\n")
    L.append("| Indicateur | Valeur | Indicateur | Valeur |")
    L.append("|---|---|---|---|")
    wr = etat["stats"]["gagnants"]/etat["stats"]["clotures"] if etat["stats"]["clotures"] else None
    L.append(f"| Perf. annualisée | {fpct(p['cagr']) if p['cagr'] is not None else '— (trop tôt)'} | Volatilité ann. | {fpct(p['vol'], False)} |")
    L.append(f"| Drawdown max | {fpct(p['maxDD'], False)} | Sharpe | {fnum(p['sharpe'],2) if p['sharpe'] is not None else '—'} |")
    L.append(f"| Exposition | {fpct(invested/equity if equity else 0, False, 0)} | Liquidités | {feur(etat['cashEUR'])} |")
    L.append(f"| Trades clôturés | {etat['stats']['clotures']}" + (f" ({round(wr*100)} % gagnants)" if wr is not None else "") + f" | Frais cumulés | {feur(etat['stats']['frais'])} |")
    L.append(f"| EUR/USD | {fnum(fx,4)} | P&L réalisé | {feur(etat['stats']['realise'])} |\n")
    L.append("## Positions\n")
    if lignes:
        L.append("| Actif | Qté | Cours | Valeur | P&L | Poids |")
        L.append("|---|---|---|---|---|---|")
        for r in lignes:
            L.append(f"| **{r['s']}** {r['nom']} | {fnum(r['qty'],3)} | {fnum(r['px'],2)} $ | {feur(r['val'])} | {fpct(r['pnlPct'])} | {round(r['poids']*100)} % |")
        L.append("")
    else:
        L.append("_Aucune position — le bot est en liquidités (aucun actif ne passe ses filtres)._\n")
    L.append("## Signaux (classement momentum)\n")
    L.append("| # | Actif | Momentum | Tendance | Cible |")
    L.append("|---|---|---|---|---|")
    for i, a in enumerate(sig[:8], 1):
        L.append(f"| {i} | **{a['s']}** {NOM[a['s']][0]} | {fpct(a['mom'])} | {'▲' if a['trend'] else '▽'} | {str(round(tgt[a['s']]*100))+' %' if a['s'] in tgt else '—'} |")
    L.append("")
    if etat["trades"]:
        L.append("## Derniers ordres\n")
        L.append("| Date | Sens | Actif | Montant | P&L | Raison |")
        L.append("|---|---|---|---|---|---|")
        for tr in etat["trades"][:12]:
            pl = fpct(None) if tr["pnl"] is None else ("+" if tr["pnl"]>=0 else "") + feur(tr["pnl"])
            L.append(f"| {fdate(tr['t'])} | {tr['sens']} | **{tr['sym']}** | {feur(tr['valEUR'])} | {pl if tr['pnl'] is not None else '—'} | {tr['raison']} |")
        L.append("")
    L.append("## Journal\n")
    for l in etat["journal"][:6]:
        L.append(f"- `{fdate(l['t'])}` — {l['msg']}")
    L.append("\n---\n_Stratégie : momentum 3 & 6 mois, filtre MM100, Top 5 pondéré inverse-volatilité (max 25 %/ligne),"
             " bande 4 %, frais 0,10 %/ordre (min 1 €), arbitrage au plus toutes les 6 h."
             " Passage horaire via GitHub Actions._\n\n"
             "_Outil pédagogique : aucun argent réel, aucune garantie de performance, pas un conseil en investissement._")
    open("README.md", "w", encoding="utf-8").write("\n".join(L))

# ── Cycle principal ───────────────────────────────────────────────────
def main():
    force = os.environ.get("BOUSSOLE_FORCE") == "1" or "--force" in sys.argv
    now = now_ms()
    if os.path.exists(ETAT):
        etat = json.load(open(ETAT, encoding="utf-8"))
    else:
        etat = dict(v=1, creeLe=now, dernierArbitrage=0, cashEUR=CFG["capital"],
                    fx=1.10, positions={}, bench=None,
                    stats=dict(clotures=0, gagnants=0, realise=0.0, frais=0.0),
                    histo=[], trades=[], lastPx={},
                    journal=[dict(t=now, msg="Bot initialisé · capital 10 000 €")])

    # 1) Cours
    data, ok = {}, 0
    for s, _, _ in UNIVERSE:
        d = fetch(s)
        if d: data[s] = d; ok += 1
        time.sleep(0.12)
    fxd = fetch("EURUSD=X")
    fx = fxd["px"] if fxd else etat.get("fx", 1.10)
    etat["fx"] = fx
    today = int(time.time()//DAY)

    # 2) Cotations utilisables (secours : dernier cours connu)
    q, sig = {}, []
    for s, n, c in UNIVERSE:
        if s in data:
            d = data[s]
            gap = today - d["closes"][-1][0]
            q[s] = dict(px=d["px"], prev=d["prev"], usable=gap <= CFG["staleDays"], src="direct")
            etat["lastPx"][s] = dict(px=d["px"], prev=d["prev"], jour=today)
        elif s in etat["lastPx"]:
            lp = etat["lastPx"][s]
            q[s] = dict(px=lp["px"], prev=lp["prev"], usable=(today-lp["jour"]) <= CFG["staleDays"], src="mémoire")
    mode_src = "directes" if ok == len(UNIVERSE) else (f"directes ({ok}/{len(UNIVERSE)})" if ok else "dernier cours connu")

    # 3) Signaux
    assets = []
    for s, n, c in UNIVERSE:
        if s not in q: continue
        if s in data:
            px_series = [c2 for _, c2 in data[s]["closes"]]
            if data[s]["closes"][-1][0] >= today: px_series[-1] = q[s]["px"]
            else: px_series.append(q[s]["px"])
            ind = indicateurs(px_series)
        else:
            ind = dict(mom=None, trend=False, vol=0.25, eligible=False)
        assets.append(dict(s=s, usable=q[s]["usable"], **ind))
    sig = sorted(assets, key=lambda a: -(a["mom"] if a["mom"] is not None else -9))

    if etat["bench"] is None and BENCH in q:
        etat["bench"] = dict(p0=q[BENCH]["px"], fx0=fx)

    # 4) Arbitrage
    usables = sum(1 for a in assets if a["usable"])
    peut = usables >= math.ceil(len(UNIVERSE)*0.7)
    du = force or now - etat["dernierArbitrage"] > CFG["cooldownH"]*3600e3
    tgt, _ = cibles(assets)
    if du and peut:
        pos, cash, trades, tgt = arbitrer(etat, q, assets, fx, now)
        etat["positions"], etat["cashEUR"] = pos, cash
        if trades:
            etat["trades"] = (trades + etat["trades"])[:400]
        etat["journal"] = ([dict(t=now, msg=f"{len(trades)} ordre{'s' if len(trades)>1 else ''} exécuté{'s' if len(trades)>1 else ''}"
                                 if trades else "Portefeuille déjà aligné — aucun ordre")] + etat["journal"])[:40]
        etat["dernierArbitrage"] = now
    elif du and not peut:
        etat["journal"] = ([dict(t=now, msg="Cours trop incertains : arbitrage reporté")] + etat["journal"])[:40]

    # 5) Valorisation + instantané
    lignes, invested = [], 0.0
    for s, p in etat["positions"].items():
        if s not in q: continue
        pE = q[s]["px"]/fx
        val = p["qty"]*pE
        invested += val
        lignes.append(dict(s=s, nom=NOM[s][0], qty=p["qty"], px=q[s]["px"], val=val,
                           pnlPct=val/p["costEUR"]-1 if p["costEUR"] > 0 else 0.0, poids=0.0))
    equity = etat["cashEUR"] + invested
    for r in lignes: r["poids"] = r["val"]/equity if equity else 0
    lignes.sort(key=lambda r: -r["val"])
    benchV = None
    if etat["bench"] and BENCH in q:
        benchV = CFG["capital"] * (q[BENCH]["px"]/etat["bench"]["p0"]) * (etat["bench"]["fx0"]/fx)
    etat["histo"].append(dict(t=now, eq=round(equity, 2), bench=round(benchV, 2) if benchV else None))
    if len(etat["histo"]) > 4000:
        h = etat["histo"]; etat["histo"] = h[:len(h)//2][::2] + h[len(h)//2:]
    etat["majLe"] = now
    etat["schema"] = 2
    etat["signaux"] = [dict(s=a["s"], mom=a["mom"], trend=a["trend"], vol=round(a["vol"], 4),
                            px=q[a["s"]]["px"], prev=q[a["s"]]["prev"],
                            cible=round(tgt.get(a["s"], 0), 4))
                       for a in sig if a["s"] in q]

    # 6) Sorties
    p = perf(etat["histo"], etat["creeLe"], equity)
    json.dump(etat, open(ETAT, "w", encoding="utf-8"), ensure_ascii=False)
    ac = courbe(etat["histo"])
    rapport(etat, lignes, equity, invested, p, sig, tgt, fx, ac, mode_src)
    print(f"OK · {mode_src} · valeur {feur(equity)} ({fpct(p['totalR'])}) · "
          f"{len(etat['positions'])} positions · dernier ordre {fdate(etat['trades'][0]['t']) if etat['trades'] else '—'}")

if __name__ == "__main__":
    main()
