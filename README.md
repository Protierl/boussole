# 🧭 BOUSSOLE — bot 24h/24

**SIMULATION · cours réels · capital fictif** — mis à jour le 27/08/2026 à 11:53 (Paris) · sources : directes

## 🔴 9 193,75 €

**-806,25 € (-8,1 %)** · jour -0,1 % depuis le 12/07/2026

![Courbe de performance](courbe.png)

| Indicateur | Valeur | Indicateur | Valeur |
|---|---|---|---|
| Perf. annualisée | -48,7 % | Volatilité ann. | 11,6 % |
| Drawdown max | -8,6 % | Sharpe | -3,94 |
| Exposition | 92 % | Liquidités | 733,62 € |
| Trades clôturés | 61 (30 % gagnants) | Frais cumulés | 215,86 € |
| EUR/USD | 1,1650 | P&L réalisé | -803,21 € |

## Positions

| Actif | Qté | Cours | Valeur | P&L | Poids |
|---|---|---|---|---|---|
| **JPM** JPMorgan | 7,713 | 356,50 $ | 2 360,32 € | +0,5 % | 26 % |
| **DBC** Panier mat. prem. | 86,702 | 30,50 $ | 2 269,89 € | -1,8 % | 25 % |
| **MSFT** Microsoft | 3,630 | 496,37 $ | 1 546,78 € | +5,7 % | 17 % |
| **AAPL** Apple | 4,963 | 313,45 $ | 1 335,28 € | -0,1 % | 15 % |
| **AMZN** Amazon | 4,243 | 260,28 $ | 947,87 € | -5,5 % | 10 % |

## Signaux (classement momentum)

| # | Actif | Momentum | Tendance | Cible |
|---|---|---|---|---|
| 1 | **USO** Pétrole WTI | +28,5 % | ▽ | — |
| 2 | **MSFT** Microsoft | +19,9 % | ▲ | 17 % |
| 3 | **JPM** JPMorgan | +18,3 % | ▲ | 25 % |
| 4 | **DBC** Panier mat. prem. | +12,9 % | ▲ | 22 % |
| 5 | **AMZN** Amazon | +10,1 % | ▲ | 8 % |
| 6 | **AAPL** Apple | +7,6 % | ▲ | 15 % |
| 7 | **QQQ** Nasdaq 100 | +6,7 % | ▲ | — |
| 8 | **SPY** S&P 500 | +6,3 % | ▲ | — |

## Derniers ordres

| Date | Sens | Actif | Montant | P&L | Raison |
|---|---|---|---|---|---|
| 27/08 11:53 | VENTE | **USO** | 1 092,29 € | -10,77 € | Filtre de tendance (< MM100) |
| 27/08 11:53 | ACHAT | **AAPL** | 1 335,28 € | — | Entrée momentum · rang 5 |
| 27/08 11:53 | ACHAT | **MSFT** | 485,05 € | — | Renforcement vers 17 % |
| 26/08 19:50 | VENTE | **AAPL** | 1 783,30 € | +16,58 € | Sorti du Top 5 |
| 26/08 19:50 | ACHAT | **USO** | 1 100,86 € | — | Entrée momentum · rang 1 |
| 25/08 22:48 | VENTE | **USO** | 965,21 € | -36,07 € | Filtre de tendance (< MM100) |
| 25/08 22:48 | ACHAT | **AAPL** | 1 763,17 € | — | Entrée momentum · rang 5 |
| 20/08 21:47 | VENTE | **AAPL** | 1 932,29 € | -27,44 € | Sorti du Top 5 |
| 20/08 21:47 | ACHAT | **DBC** | 2 308,62 € | — | Entrée momentum · rang 4 |
| 20/08 15:13 | VENTE | **DBC** | 2 326,82 € | -14,34 € | Sorti du Top 5 |
| 20/08 15:13 | ACHAT | **AAPL** | 1 955,84 € | — | Entrée momentum · rang 5 |
| 18/08 15:58 | VENTE | **QQQ** | 2 309,98 € | -40,39 € | Sorti du Top 5 |

## Journal

- `27/08 11:53` — 3 ordres exécutés
- `26/08 19:50` — 2 ordres exécutés
- `26/08 11:59` — Portefeuille déjà aligné — aucun ordre
- `26/08 05:26` — Portefeuille déjà aligné — aucun ordre
- `25/08 22:48` — 2 ordres exécutés
- `25/08 16:06` — Portefeuille déjà aligné — aucun ordre

---
_Stratégie : momentum 3 & 6 mois, filtre MM100, Top 5 pondéré inverse-volatilité (max 25 %/ligne), bande 4 %, frais 0,10 %/ordre (min 1 €), arbitrage au plus toutes les 6 h. Passage horaire via GitHub Actions._

_Outil pédagogique : aucun argent réel, aucune garantie de performance, pas un conseil en investissement._