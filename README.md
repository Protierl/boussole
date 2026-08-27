# 🧭 BOUSSOLE — bot 24h/24

**SIMULATION · cours réels · capital fictif** — mis à jour le 27/08/2026 à 22:33 (Paris) · sources : directes

## 🔴 9 214,71 €

**-785,29 € (-7,9 %)** · jour +0,2 % depuis le 12/07/2026

![Courbe de performance](courbe.png)

| Indicateur | Valeur | Indicateur | Valeur |
|---|---|---|---|
| Perf. annualisée | -47,5 % | Volatilité ann. | 11,6 % |
| Drawdown max | -8,6 % | Sharpe | -3,82 |
| Exposition | 88 % | Liquidités | 1 061,05 € |
| Trades clôturés | 63 (30 % gagnants) | Frais cumulés | 220,21 € |
| EUR/USD | 1,1655 | P&L réalisé | -873,07 € |

## Positions

| Actif | Qté | Cours | Valeur | P&L | Poids |
|---|---|---|---|---|---|
| **JPM** JPMorgan | 7,713 | 354,22 $ | 2 344,21 € | -0,2 % | 25 % |
| **DBC** Panier mat. prem. | 86,702 | 30,86 $ | 2 295,70 € | -0,7 % | 25 % |
| **MSFT** Microsoft | 3,630 | 505,06 $ | 1 573,18 € | +7,5 % | 17 % |
| **NVDA** Nvidia | 5,154 | 227,98 $ | 1 008,10 € | -0,1 % | 11 % |
| **USO** Pétrole WTI | 8,359 | 130,01 $ | 932,47 € | -0,1 % | 10 % |

## Signaux (classement momentum)

| # | Actif | Momentum | Tendance | Cible |
|---|---|---|---|---|
| 1 | **USO** Pétrole WTI | +31,2 % | ▲ | 10 % |
| 2 | **MSFT** Microsoft | +22,0 % | ▲ | 17 % |
| 3 | **JPM** JPMorgan | +17,5 % | ▲ | 25 % |
| 4 | **NVDA** Nvidia | +14,9 % | ▲ | 11 % |
| 5 | **DBC** Panier mat. prem. | +14,2 % | ▲ | 22 % |
| 6 | **AMZN** Amazon | +8,4 % | ▲ | — |
| 7 | **QQQ** Nasdaq 100 | +8,2 % | ▲ | — |
| 8 | **AAPL** Apple | +8,0 % | ▲ | — |

## Derniers ordres

| Date | Sens | Actif | Montant | P&L | Raison |
|---|---|---|---|---|---|
| 27/08 22:33 | VENTE | **AMZN** | 932,83 € | -71,42 € | Sorti du Top 5 |
| 27/08 22:33 | VENTE | **AAPL** | 1 339,52 € | +1,56 € | Sorti du Top 5 |
| 27/08 22:33 | ACHAT | **NVDA** | 1 008,10 € | — | Entrée momentum · rang 4 |
| 27/08 22:33 | ACHAT | **USO** | 932,47 € | — | Entrée momentum · rang 1 |
| 27/08 11:53 | VENTE | **USO** | 1 092,29 € | -10,77 € | Filtre de tendance (< MM100) |
| 27/08 11:53 | ACHAT | **AAPL** | 1 335,28 € | — | Entrée momentum · rang 5 |
| 27/08 11:53 | ACHAT | **MSFT** | 485,05 € | — | Renforcement vers 17 % |
| 26/08 19:50 | VENTE | **AAPL** | 1 783,30 € | +16,58 € | Sorti du Top 5 |
| 26/08 19:50 | ACHAT | **USO** | 1 100,86 € | — | Entrée momentum · rang 1 |
| 25/08 22:48 | VENTE | **USO** | 965,21 € | -36,07 € | Filtre de tendance (< MM100) |
| 25/08 22:48 | ACHAT | **AAPL** | 1 763,17 € | — | Entrée momentum · rang 5 |
| 20/08 21:47 | VENTE | **AAPL** | 1 932,29 € | -27,44 € | Sorti du Top 5 |

## Journal

- `27/08 22:33` — 4 ordres exécutés
- `27/08 11:53` — 3 ordres exécutés
- `26/08 19:50` — 2 ordres exécutés
- `26/08 11:59` — Portefeuille déjà aligné — aucun ordre
- `26/08 05:26` — Portefeuille déjà aligné — aucun ordre
- `25/08 22:48` — 2 ordres exécutés

---
_Stratégie : momentum 3 & 6 mois, filtre MM100, Top 5 pondéré inverse-volatilité (max 25 %/ligne), bande 4 %, frais 0,10 %/ordre (min 1 €), arbitrage au plus toutes les 6 h. Passage horaire via GitHub Actions._

_Outil pédagogique : aucun argent réel, aucune garantie de performance, pas un conseil en investissement._