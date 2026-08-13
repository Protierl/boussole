# 🧭 BOUSSOLE — bot 24h/24

**SIMULATION · cours réels · capital fictif** — mis à jour le 13/08/2026 à 17:17 (Paris) · sources : directes

## 🔴 9 493,91 €

**-506,09 € (-5,1 %)** · jour -0,5 % depuis le 12/07/2026

![Courbe de performance](courbe.png)

| Indicateur | Valeur | Indicateur | Valeur |
|---|---|---|---|
| Perf. annualisée | -44,6 % | Volatilité ann. | 13,3 % |
| Drawdown max | -6,9 % | Sharpe | -3,04 |
| Exposition | 83 % | Liquidités | 1 659,80 € |
| Trades clôturés | 47 (30 % gagnants) | Frais cumulés | 163,75 € |
| EUR/USD | 1,1541 | P&L réalisé | -617,24 € |

## Positions

| Actif | Qté | Cours | Valeur | P&L | Poids |
|---|---|---|---|---|---|
| **JPM** JPMorgan | 7,713 | 362,18 $ | 2 420,57 € | +3,0 % | 25 % |
| **DBC** Panier mat. prem. | 91,376 | 29,91 $ | 2 367,73 € | -0,9 % | 25 % |
| **MSFT** Microsoft | 2,492 | 495,73 $ | 1 070,36 € | +9,5 % | 11 % |
| **USO** Pétrole WTI | 9,089 | 126,34 $ | 995,07 € | -0,9 % | 10 % |
| **AMZN** Amazon | 4,243 | 266,69 $ | 980,39 € | -2,3 % | 10 % |

## Signaux (classement momentum)

| # | Actif | Momentum | Tendance | Cible |
|---|---|---|---|---|
| 1 | **USO** Pétrole WTI | +24,6 % | ▽ | — |
| 2 | **MSFT** Microsoft | +22,5 % | ▲ | 10 % |
| 3 | **JPM** JPMorgan | +18,6 % | ▲ | 25 % |
| 4 | **AMZN** Amazon | +14,7 % | ▲ | 9 % |
| 5 | **DBC** Panier mat. prem. | +11,6 % | ▲ | 21 % |
| 6 | **QQQ** Nasdaq 100 | +11,0 % | ▲ | 25 % |
| 7 | **NVDA** Nvidia | +9,0 % | ▲ | — |
| 8 | **SPY** S&P 500 | +8,5 % | ▲ | — |

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