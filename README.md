# 🧭 BOUSSOLE — bot 24h/24

**SIMULATION · cours réels · capital fictif** — mis à jour le 30/07/2026 à 00:15 (Paris) · sources : directes

## 🔴 9 564,18 €

**-435,82 € (-4,4 %)** · jour -0,0 % depuis le 12/07/2026

![Courbe de performance](courbe.png)

| Indicateur | Valeur | Indicateur | Valeur |
|---|---|---|---|
| Perf. annualisée | -60,7 % | Volatilité ann. | 15,6 % |
| Drawdown max | -4,6 % | Sharpe | -3,97 |
| Exposition | 79 % | Liquidités | 2 020,15 € |
| Trades clôturés | 31 (23 % gagnants) | Frais cumulés | 104,12 € |
| EUR/USD | 1,1472 | P&L réalisé | -406,85 € |

## Positions

| Actif | Qté | Cours | Valeur | P&L | Poids |
|---|---|---|---|---|---|
| **SPY** S&P 500 | 3,766 | 729,46 $ | 2 394,50 € | -2,1 % | 25 % |
| **JPM** JPMorgan | 6,086 | 344,71 $ | 1 828,62 € | -1,4 % | 19 % |
| **DBC** Panier mat. prem. | 61,933 | 29,42 $ | 1 588,27 € | -0,7 % | 17 % |
| **AAPL** Apple | 3,691 | 338,19 $ | 1 088,14 € | +6,7 % | 11 % |
| **USO** Pétrole WTI | 5,718 | 129,31 $ | 644,50 € | -1,3 % | 7 % |

## Signaux (classement momentum)

| # | Actif | Momentum | Tendance | Cible |
|---|---|---|---|---|
| 1 | **USO** Pétrole WTI | +31,8 % | ▲ | 7 % |
| 2 | **AAPL** Apple | +27,9 % | ▲ | 15 % |
| 3 | **JPM** JPMorgan | +12,7 % | ▲ | 18 % |
| 4 | **DBC** Panier mat. prem. | +8,2 % | ▲ | 17 % |
| 5 | **SPY** S&P 500 | +3,7 % | ▲ | 25 % |
| 6 | **QQQ** Nasdaq 100 | +2,7 % | ▽ | — |
| 7 | **EZU** Zone euro | +1,2 % | ▲ | — |
| 8 | **EEM** Marchés émergents | -0,9 % | ▽ | — |

## Derniers ordres

| Date | Sens | Actif | Montant | P&L | Raison |
|---|---|---|---|---|---|
| 29/07 17:20 | VENTE | **QQQ** | 1 511,57 € | -32,52 € | Filtre de tendance (< MM100) |
| 29/07 17:20 | VENTE | **EZU** | 1 862,27 € | -24,54 € | Sorti du Top 5 |
| 29/07 17:20 | ACHAT | **DBC** | 1 598,10 € | — | Entrée momentum · rang 4 |
| 29/07 17:20 | ACHAT | **USO** | 651,85 € | — | Entrée momentum · rang 1 |
| 29/07 02:10 | VENTE | **AAPL** | 398,67 € | +28,69 € | Allègement vers 11 % |
| 28/07 05:39 | VENTE | **DBC** | 1 620,47 € | +9,02 € | Filtre de tendance (< MM100) |
| 28/07 05:39 | ACHAT | **EZU** | 1 883,06 € | — | Entrée momentum · rang 5 |
| 27/07 20:49 | VENTE | **DBC** | 834,44 € | +6,84 € | Allègement vers 17 % |
| 27/07 20:49 | VENTE | **USO** | 1 107,73 € | +19,31 € | Filtre de tendance (< MM100) |
| 27/07 20:49 | VENTE | **JPM** | 547,61 € | +11,73 € | Allègement vers 19 % |
| 27/07 20:49 | VENTE | **NVDA** | 1 397,12 € | -69,78 € | Momentum devenu négatif |
| 27/07 20:49 | ACHAT | **SPY** | 2 442,23 € | — | Entrée momentum · rang 5 |

## Journal

- `30/07 00:15` — Portefeuille déjà aligné — aucun ordre
- `29/07 17:20` — 4 ordres exécutés
- `29/07 08:46` — Portefeuille déjà aligné — aucun ordre
- `29/07 02:10` — 1 ordre exécuté
- `28/07 18:52` — Portefeuille déjà aligné — aucun ordre
- `28/07 11:49` — Portefeuille déjà aligné — aucun ordre

---
_Stratégie : momentum 3 & 6 mois, filtre MM100, Top 5 pondéré inverse-volatilité (max 25 %/ligne), bande 4 %, frais 0,10 %/ordre (min 1 €), arbitrage au plus toutes les 6 h. Passage horaire via GitHub Actions._

_Outil pédagogique : aucun argent réel, aucune garantie de performance, pas un conseil en investissement._