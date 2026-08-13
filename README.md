# 🧭 BOUSSOLE — bot 24h/24

**SIMULATION · cours réels · capital fictif** — mis à jour le 13/08/2026 à 18:13 (Paris) · sources : directes

## 🔴 9 499,81 €

**-500,19 € (-5,0 %)** · jour -0,5 % depuis le 12/07/2026

![Courbe de performance](courbe.png)

| Indicateur | Valeur | Indicateur | Valeur |
|---|---|---|---|
| Perf. annualisée | -44,1 % | Volatilité ann. | 13,2 % |
| Drawdown max | -6,9 % | Sharpe | -3,01 |
| Exposition | 83 % | Liquidités | 1 659,80 € |
| Trades clôturés | 47 (30 % gagnants) | Frais cumulés | 163,75 € |
| EUR/USD | 1,1533 | P&L réalisé | -617,24 € |

## Positions

| Actif | Qté | Cours | Valeur | P&L | Poids |
|---|---|---|---|---|---|
| **JPM** JPMorgan | 7,713 | 362,77 $ | 2 426,20 € | +3,3 % | 26 % |
| **DBC** Panier mat. prem. | 91,376 | 29,93 $ | 2 371,35 € | -0,7 % | 25 % |
| **MSFT** Microsoft | 2,492 | 494,23 $ | 1 067,87 € | +9,3 % | 11 % |
| **USO** Pétrole WTI | 9,089 | 126,76 $ | 999,00 € | -0,6 % | 11 % |
| **AMZN** Amazon | 4,243 | 265,20 $ | 975,59 € | -2,8 % | 10 % |

## Signaux (classement momentum)

| # | Actif | Momentum | Tendance | Cible |
|---|---|---|---|---|
| 1 | **USO** Pétrole WTI | +25,0 % | ▽ | — |
| 2 | **MSFT** Microsoft | +22,1 % | ▲ | 10 % |
| 3 | **JPM** JPMorgan | +18,8 % | ▲ | 25 % |
| 4 | **AMZN** Amazon | +14,1 % | ▲ | 9 % |
| 5 | **QQQ** Nasdaq 100 | +10,8 % | ▲ | 24 % |
| 6 | **DBC** Panier mat. prem. | +9,1 % | ▲ | 22 % |
| 7 | **NVDA** Nvidia | +8,9 % | ▲ | — |
| 8 | **SPY** S&P 500 | +8,3 % | ▲ | — |

## Derniers ordres

| Date | Sens | Actif | Montant | P&L | Raison |
|---|---|---|---|---|---|
| 13/08 07:08 | VENTE | **QQQ** | 2 408,26 € | +16,20 € | Sorti du Top 5 |
| 13/08 07:08 | ACHAT | **DBC** | 2 386,44 € | — | Entrée momentum · rang 5 |
| 12/08 23:04 | VENTE | **NVDA** | 1 552,49 € | +7,70 € | Sorti du Top 5 |
| 12/08 23:04 | ACHAT | **USO** | 1 003,55 € | — | Entrée momentum · rang 1 |
| 12/08 15:50 | VENTE | **USO** | 1 023,99 € | -8,61 € | Filtre de tendance (< MM100) |
| 12/08 15:50 | ACHAT | **NVDA** | 1 541,69 € | — | Entrée momentum · rang 5 |
| 12/08 02:01 | VENTE | **DBC** | 2 413,24 € | +15,58 € | Sorti du Top 5 |
| 12/08 02:01 | ACHAT | **QQQ** | 2 387,27 € | — | Entrée momentum · rang 5 |
| 11/08 19:14 | VENTE | **QQQ** | 2 336,59 € | -15,75 € | Sorti du Top 5 |
| 11/08 19:14 | ACHAT | **USO** | 1 030,55 € | — | Entrée momentum · rang 1 |
| 11/08 00:00 | VENTE | **NVDA** | 1 469,39 € | +37,97 € | Sorti du Top 5 |
| 11/08 00:00 | ACHAT | **QQQ** | 2 347,65 € | — | Entrée momentum · rang 5 |

## Journal

- `13/08 14:01` — Portefeuille déjà aligné — aucun ordre
- `13/08 07:08` — 2 ordres exécutés
- `12/08 23:04` — 2 ordres exécutés
- `12/08 15:50` — 2 ordres exécutés
- `12/08 08:44` — Portefeuille déjà aligné — aucun ordre
- `12/08 02:01` — 2 ordres exécutés

---
_Stratégie : momentum 3 & 6 mois, filtre MM100, Top 5 pondéré inverse-volatilité (max 25 %/ligne), bande 4 %, frais 0,10 %/ordre (min 1 €), arbitrage au plus toutes les 6 h. Passage horaire via GitHub Actions._

_Outil pédagogique : aucun argent réel, aucune garantie de performance, pas un conseil en investissement._