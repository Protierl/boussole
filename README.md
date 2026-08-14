# 🧭 BOUSSOLE — bot 24h/24

**SIMULATION · cours réels · capital fictif** — mis à jour le 14/08/2026 à 21:15 (Paris) · sources : directes

## 🔴 9 433,16 €

**-566,84 € (-5,7 %)** · jour -0,4 % depuis le 12/07/2026

![Courbe de performance](courbe.png)

| Indicateur | Valeur | Indicateur | Valeur |
|---|---|---|---|
| Perf. annualisée | -47,3 % | Volatilité ann. | 13,1 % |
| Drawdown max | -6,9 % | Sharpe | -3,35 |
| Exposition | 94 % | Liquidités | 538,65 € |
| Trades clôturés | 51 (27 % gagnants) | Frais cumulés | 178,04 € |
| EUR/USD | 1,1570 | P&L réalisé | -681,18 € |

## Positions

| Actif | Qté | Cours | Valeur | P&L | Poids |
|---|---|---|---|---|---|
| **JPM** JPMorgan | 7,713 | 363,13 $ | 2 420,84 € | +3,1 % | 26 % |
| **QQQ** Nasdaq 100 | 3,733 | 729,62 $ | 2 354,08 € | -0,8 % | 25 % |
| **DBC** Panier mat. prem. | 80,575 | 30,00 $ | 2 088,90 € | +0,5 % | 22 % |
| **MSFT** Microsoft | 2,492 | 495,09 $ | 1 066,31 € | +9,1 % | 11 % |
| **AMZN** Amazon | 4,243 | 263,00 $ | 964,39 € | -3,9 % | 10 % |

## Signaux (classement momentum)

| # | Actif | Momentum | Tendance | Cible |
|---|---|---|---|---|
| 1 | **USO** Pétrole WTI | +27,0 % | ▽ | — |
| 2 | **MSFT** Microsoft | +22,1 % | ▲ | 10 % |
| 3 | **JPM** JPMorgan | +20,5 % | ▲ | 25 % |
| 4 | **AMZN** Amazon | +15,1 % | ▲ | 9 % |
| 5 | **QQQ** Nasdaq 100 | +11,4 % | ▲ | 25 % |
| 6 | **DBC** Panier mat. prem. | +10,1 % | ▲ | 20 % |
| 7 | **AAPL** Apple | +9,6 % | ▲ | — |
| 8 | **SPY** S&P 500 | +8,8 % | ▲ | — |

## Derniers ordres

| Date | Sens | Actif | Montant | P&L | Raison |
|---|---|---|---|---|---|
| 14/08 12:18 | VENTE | **AAPL** | 1 703,68 € | -6,22 € | Sorti du Top 5 |
| 14/08 12:18 | ACHAT | **DBC** | 2 076,08 € | — | Entrée momentum · rang 5 |
| 14/08 04:48 | VENTE | **NVDA** | 1 538,13 € | -4,15 € | Sorti du Top 5 |
| 14/08 04:48 | ACHAT | **AAPL** | 1 706,49 € | — | Entrée momentum · rang 5 |
| 13/08 20:11 | VENTE | **USO** | 984,49 € | -21,06 € | Filtre de tendance (< MM100) |
| 13/08 20:11 | VENTE | **DBC** | 2 358,67 € | -32,51 € | Sorti du Top 5 |
| 13/08 20:11 | ACHAT | **QQQ** | 2 370,06 € | — | Entrée momentum · rang 4 |
| 13/08 20:11 | ACHAT | **NVDA** | 1 539,21 € | — | Entrée momentum · rang 5 |
| 13/08 07:08 | VENTE | **QQQ** | 2 408,26 € | +16,20 € | Sorti du Top 5 |
| 13/08 07:08 | ACHAT | **DBC** | 2 386,44 € | — | Entrée momentum · rang 5 |
| 12/08 23:04 | VENTE | **NVDA** | 1 552,49 € | +7,70 € | Sorti du Top 5 |
| 12/08 23:04 | ACHAT | **USO** | 1 003,55 € | — | Entrée momentum · rang 1 |

## Journal

- `14/08 19:13` — Portefeuille déjà aligné — aucun ordre
- `14/08 12:18` — 2 ordres exécutés
- `14/08 04:48` — 2 ordres exécutés
- `13/08 20:11` — 4 ordres exécutés
- `13/08 14:01` — Portefeuille déjà aligné — aucun ordre
- `13/08 07:08` — 2 ordres exécutés

---
_Stratégie : momentum 3 & 6 mois, filtre MM100, Top 5 pondéré inverse-volatilité (max 25 %/ligne), bande 4 %, frais 0,10 %/ordre (min 1 €), arbitrage au plus toutes les 6 h. Passage horaire via GitHub Actions._

_Outil pédagogique : aucun argent réel, aucune garantie de performance, pas un conseil en investissement._