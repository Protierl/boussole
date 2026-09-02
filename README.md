# 🧭 BOUSSOLE — bot 24h/24

**SIMULATION · cours réels · capital fictif** — mis à jour le 02/09/2026 à 13:23 (Paris) · sources : directes

## 🔴 9 220,65 €

**-779,35 € (-7,8 %)** · jour +0,1 % depuis le 12/07/2026

![Courbe de performance](courbe.png)

| Indicateur | Valeur | Indicateur | Valeur |
|---|---|---|---|
| Perf. annualisée | -43,4 % | Volatilité ann. | 11,2 % |
| Drawdown max | -8,6 % | Sharpe | -3,46 |
| Exposition | 95 % | Liquidités | 458,37 € |
| Trades clôturés | 73 (26 % gagnants) | Frais cumulés | 252,57 € |
| EUR/USD | 1,1581 | P&L réalisé | -1 032,42 € |

## Positions

| Actif | Qté | Cours | Valeur | P&L | Poids |
|---|---|---|---|---|---|
| **JPM** JPMorgan | 7,713 | 354,95 $ | 2 364,06 € | +0,6 % | 26 % |
| **DBC** Panier mat. prem. | 71,098 | 31,93 $ | 1 960,24 € | +2,2 % | 21 % |
| **AAPL** Apple | 6,588 | 325,13 $ | 1 849,66 € | +0,2 % | 20 % |
| **MSFT** Microsoft | 3,630 | 501,02 $ | 1 570,57 € | +7,3 % | 17 % |
| **USO** Pétrole WTI | 8,359 | 141,00 $ | 1 017,75 € | +9,0 % | 11 % |

## Signaux (classement momentum)

| # | Actif | Momentum | Tendance | Cible |
|---|---|---|---|---|
| 1 | **USO** Pétrole WTI | +27,0 % | ▲ | 9 % |
| 2 | **MSFT** Microsoft | +20,4 % | ▲ | 17 % |
| 3 | **JPM** JPMorgan | +18,1 % | ▲ | 25 % |
| 4 | **DBC** Panier mat. prem. | +14,6 % | ▲ | 20 % |
| 5 | **AAPL** Apple | +14,3 % | ▲ | 20 % |
| 6 | **NVDA** Nvidia | +10,0 % | ▲ | — |
| 7 | **AMZN** Amazon | +9,8 % | ▲ | — |
| 8 | **SPY** S&P 500 | +6,1 % | ▲ | — |

## Derniers ordres

| Date | Sens | Actif | Montant | P&L | Raison |
|---|---|---|---|---|---|
| 01/09 16:56 | VENTE | **AMZN** | 1 419,90 € | -29,88 € | Filtre de tendance (< MM100) |
| 01/09 16:56 | ACHAT | **AAPL** | 1 843,64 € | — | Entrée momentum · rang 5 |
| 01/09 07:14 | VENTE | **NVDA** | 971,69 € | -0,10 € | Sorti du Top 5 |
| 01/09 07:14 | ACHAT | **AMZN** | 1 446,91 € | — | Entrée momentum · rang 4 |
| 31/08 22:08 | VENTE | **AMZN** | 1 405,88 € | -43,00 € | Sorti du Top 5 |
| 31/08 22:08 | ACHAT | **NVDA** | 969,79 € | — | Entrée momentum · rang 5 |
| 31/08 15:57 | VENTE | **AAPL** | 2 108,74 € | -21,23 € | Sorti du Top 5 |
| 31/08 15:57 | ACHAT | **DBC** | 1 915,96 € | — | Entrée momentum · rang 5 |
| 29/08 20:33 | VENTE | **DBC** | 2 097,57 € | -4,20 € | Sorti du Top 5 |
| 29/08 20:33 | VENTE | **NVDA** | 952,90 € | -2,00 € | Sorti du Top 5 |
| 29/08 20:33 | ACHAT | **AAPL** | 2 125,74 € | — | Entrée momentum · rang 5 |
| 29/08 20:33 | ACHAT | **AMZN** | 1 446,03 € | — | Entrée momentum · rang 4 |

## Journal

- `02/09 07:52` — Portefeuille déjà aligné — aucun ordre
- `01/09 23:49` — Portefeuille déjà aligné — aucun ordre
- `01/09 16:56` — 2 ordres exécutés
- `01/09 07:14` — 2 ordres exécutés
- `31/08 22:08` — 2 ordres exécutés
- `31/08 15:57` — 2 ordres exécutés

---
_Stratégie : momentum 3 & 6 mois, filtre MM100, Top 5 pondéré inverse-volatilité (max 25 %/ligne), bande 4 %, frais 0,10 %/ordre (min 1 €), arbitrage au plus toutes les 6 h. Passage horaire via GitHub Actions._

_Outil pédagogique : aucun argent réel, aucune garantie de performance, pas un conseil en investissement._