# 🧭 BOUSSOLE — bot 24h/24

**SIMULATION · cours réels · capital fictif** — mis à jour le 12/08/2026 à 19:15 (Paris) · sources : directes

## 🔴 9 560,23 €

**-439,77 € (-4,4 %)** · jour +0,1 % depuis le 12/07/2026

![Courbe de performance](courbe.png)

| Indicateur | Valeur | Indicateur | Valeur |
|---|---|---|---|
| Perf. annualisée | -40,9 % | Volatilité ann. | 13,4 % |
| Drawdown max | -6,9 % | Sharpe | -2,68 |
| Exposition | 89 % | Liquidités | 1 096,40 € |
| Trades clôturés | 45 (27 % gagnants) | Frais cumulés | 156,40 € |
| EUR/USD | 1,1531 | P&L réalisé | -641,14 € |

## Positions

| Actif | Qté | Cours | Valeur | P&L | Poids |
|---|---|---|---|---|---|
| **JPM** JPMorgan | 7,713 | 365,09 $ | 2 442,13 € | +4,0 % | 26 % |
| **QQQ** Nasdaq 100 | 3,837 | 724,95 $ | 2 412,00 € | +0,9 % | 25 % |
| **NVDA** Nvidia | 7,988 | 224,12 $ | 1 552,56 € | +0,6 % | 16 % |
| **MSFT** Microsoft | 2,492 | 493,68 $ | 1 066,87 € | +9,2 % | 11 % |
| **AMZN** Amazon | 4,243 | 269,14 $ | 990,27 € | -1,3 % | 10 % |

## Signaux (classement momentum)

| # | Actif | Momentum | Tendance | Cible |
|---|---|---|---|---|
| 1 | **USO** Pétrole WTI | +25,6 % | ▲ | 11 % |
| 2 | **MSFT** Microsoft | +20,3 % | ▲ | 12 % |
| 3 | **JPM** JPMorgan | +17,2 % | ▲ | 25 % |
| 4 | **AMZN** Amazon | +15,6 % | ▲ | 11 % |
| 5 | **DBC** Panier mat. prem. | +12,8 % | ▲ | 24 % |
| 6 | **QQQ** Nasdaq 100 | +10,5 % | ▲ | — |
| 7 | **NVDA** Nvidia | +10,2 % | ▲ | — |
| 8 | **SPY** S&P 500 | +8,2 % | ▲ | — |

## Derniers ordres

| Date | Sens | Actif | Montant | P&L | Raison |
|---|---|---|---|---|---|
| 12/08 15:50 | VENTE | **USO** | 1 023,99 € | -8,61 € | Filtre de tendance (< MM100) |
| 12/08 15:50 | ACHAT | **NVDA** | 1 541,69 € | — | Entrée momentum · rang 5 |
| 12/08 02:01 | VENTE | **DBC** | 2 413,24 € | +15,58 € | Sorti du Top 5 |
| 12/08 02:01 | ACHAT | **QQQ** | 2 387,27 € | — | Entrée momentum · rang 5 |
| 11/08 19:14 | VENTE | **QQQ** | 2 336,59 € | -15,75 € | Sorti du Top 5 |
| 11/08 19:14 | ACHAT | **USO** | 1 030,55 € | — | Entrée momentum · rang 1 |
| 11/08 00:00 | VENTE | **NVDA** | 1 469,39 € | +37,97 € | Sorti du Top 5 |
| 11/08 00:00 | ACHAT | **QQQ** | 2 347,65 € | — | Entrée momentum · rang 5 |
| 10/08 17:18 | VENTE | **QQQ** | 2 399,98 € | +54,89 € | Sorti du Top 5 |
| 10/08 17:18 | ACHAT | **DBC** | 2 392,86 € | — | Entrée momentum · rang 4 |
| 07/08 02:17 | VENTE | **AAPL** | 1 763,85 € | -79,51 € | Sorti du Top 5 |
| 07/08 02:17 | ACHAT | **AMZN** | 1 002,25 € | — | Entrée momentum · rang 4 |

## Journal

- `12/08 15:50` — 2 ordres exécutés
- `12/08 08:44` — Portefeuille déjà aligné — aucun ordre
- `12/08 02:01` — 2 ordres exécutés
- `11/08 19:14` — 2 ordres exécutés
- `11/08 13:07` — Portefeuille déjà aligné — aucun ordre
- `11/08 06:41` — Portefeuille déjà aligné — aucun ordre

---
_Stratégie : momentum 3 & 6 mois, filtre MM100, Top 5 pondéré inverse-volatilité (max 25 %/ligne), bande 4 %, frais 0,10 %/ordre (min 1 €), arbitrage au plus toutes les 6 h. Passage horaire via GitHub Actions._

_Outil pédagogique : aucun argent réel, aucune garantie de performance, pas un conseil en investissement._