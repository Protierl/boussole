# 🧭 BOUSSOLE — bot 24h/24

**SIMULATION · cours réels · capital fictif** — mis à jour le 05/11/2026 à 23:01 (Paris) · sources : directes

## 🔴 9 274,28 €

**-725,72 € (-7,3 %)** · jour -1,6 % depuis le 12/07/2026

![Courbe de performance](courbe.png)

| Indicateur | Valeur | Indicateur | Valeur |
|---|---|---|---|
| Perf. annualisée | -21,0 % | Volatilité ann. | 10,7 % |
| Drawdown max | -9,0 % | Sharpe | -1,48 |
| Exposition | 82 % | Liquidités | 1 696,61 € |
| Trades clôturés | 118 (36 % gagnants) | Frais cumulés | 387,13 € |
| EUR/USD | 1,1215 | P&L réalisé | -801,72 € |

## Positions

| Actif | Qté | Cours | Valeur | P&L | Poids |
|---|---|---|---|---|---|
| **AAPL** Apple | 7,558 | 344,17 $ | 2 319,34 € | +1,8 % | 25 % |
| **DBC** Panier mat. prem. | 81,856 | 31,47 $ | 2 296,93 € | -3,3 % | 25 % |
| **MSFT** Microsoft | 3,659 | 535,93 $ | 1 748,45 € | +10,7 % | 19 % |
| **USO** Pétrole WTI | 9,178 | 148,21 $ | 1 212,95 € | -4,4 % | 13 % |

## Signaux (classement momentum)

| # | Actif | Momentum | Tendance | Cible |
|---|---|---|---|---|
| 1 | **USO** Pétrole WTI | +17,7 % | ▲ | 15 % |
| 2 | **MSFT** Microsoft | +17,3 % | ▲ | 20 % |
| 3 | **AAPL** Apple | +14,8 % | ▲ | 25 % |
| 4 | **DBC** Panier mat. prem. | +6,4 % | ▲ | 25 % |
| 5 | **JPM** JPMorgan | +2,3 % | ▽ | — |
| 6 | **META** Meta | +0,1 % | ▽ | — |
| 7 | **SPY** S&P 500 | -2,5 % | ▽ | — |
| 8 | **TLT** Obligations US 20 ans | -2,7 % | ▽ | — |

## Derniers ordres

| Date | Sens | Actif | Montant | P&L | Raison |
|---|---|---|---|---|---|
| 05/11 23:01 | VENTE | **JPM** | 2 083,69 € | -85,63 € | Filtre de tendance (< MM100) |
| 05/11 23:01 | ACHAT | **AAPL** | 384,99 € | — | Renforcement vers 25 % |
| 05/11 07:53 | VENTE | **META** | 1 445,87 € | -27,93 € | Filtre de tendance (< MM100) |
| 05/11 07:53 | ACHAT | **JPM** | 2 165,07 € | — | Entrée momentum · rang 4 |
| 04/11 19:00 | VENTE | **MSFT** | 534,50 € | +64,29 € | Allègement vers 19 % |
| 04/11 19:00 | VENTE | **AAPL** | 489,78 € | +22,08 € | Allègement vers 21 % |
| 04/11 19:00 | ACHAT | **META** | 1 470,88 € | — | Entrée momentum · rang 4 |
| 03/11 16:13 | ACHAT | **USO** | 391,90 € | — | Renforcement vers 14 % |
| 03/11 00:35 | VENTE | **SPY** | 2 050,73 € | -27,85 € | Filtre de tendance (< MM100) |
| 03/11 00:35 | ACHAT | **MSFT** | 481,89 € | — | Renforcement vers 23 % |
| 02/11 17:07 | VENTE | **USO** | 421,04 € | +14,27 € | Allègement vers 10 % |
| 02/11 17:07 | ACHAT | **SPY** | 2 074,46 € | — | Entrée momentum · rang 5 |

## Journal

- `05/11 23:01` — 2 ordres exécutés
- `05/11 16:30` — Portefeuille déjà aligné — aucun ordre
- `05/11 07:53` — 2 ordres exécutés
- `04/11 19:00` — 3 ordres exécutés
- `04/11 10:20` — Portefeuille déjà aligné — aucun ordre
- `04/11 02:25` — Portefeuille déjà aligné — aucun ordre

---
_Stratégie : momentum 3 & 6 mois, filtre MM100, Top 5 pondéré inverse-volatilité (max 25 %/ligne), bande 4 %, frais 0,10 %/ordre (min 1 €), arbitrage au plus toutes les 6 h. Passage horaire via GitHub Actions._

_Outil pédagogique : aucun argent réel, aucune garantie de performance, pas un conseil en investissement._