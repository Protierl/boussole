# 🧭 BOUSSOLE — bot 24h/24

**SIMULATION · cours réels · capital fictif** — mis à jour le 29/07/2026 à 19:40 (Paris) · sources : directes

## 🔴 9 671,22 €

**-328,78 € (-3,3 %)** · jour -1,0 % depuis le 12/07/2026

![Courbe de performance](courbe.png)

| Indicateur | Valeur | Indicateur | Valeur |
|---|---|---|---|
| Perf. annualisée | -50,7 % | Volatilité ann. | 14,6 % |
| Drawdown max | -3,5 % | Sharpe | -3,37 |
| Exposition | 79 % | Liquidités | 2 020,15 € |
| Trades clôturés | 31 (23 % gagnants) | Frais cumulés | 104,12 € |
| EUR/USD | 1,1397 | P&L réalisé | -406,85 € |

## Positions

| Actif | Qté | Cours | Valeur | P&L | Poids |
|---|---|---|---|---|---|
| **SPY** S&P 500 | 3,766 | 735,66 $ | 2 430,74 € | -0,6 % | 25 % |
| **JPM** JPMorgan | 6,086 | 349,78 $ | 1 867,73 € | +0,7 % | 19 % |
| **DBC** Panier mat. prem. | 61,933 | 29,38 $ | 1 596,55 € | -0,2 % | 17 % |
| **AAPL** Apple | 3,691 | 343,17 $ | 1 111,43 € | +8,9 % | 11 % |
| **USO** Pétrole WTI | 5,718 | 128,49 $ | 644,63 € | -1,3 % | 7 % |

## Signaux (classement momentum)

| # | Actif | Momentum | Tendance | Cible |
|---|---|---|---|---|
| 1 | **USO** Pétrole WTI | +35,1 % | ▲ | 7 % |
| 2 | **AAPL** Apple | +31,3 % | ▲ | 14 % |
| 3 | **JPM** JPMorgan | +14,2 % | ▲ | 19 % |
| 4 | **DBC** Panier mat. prem. | +9,9 % | ▲ | 16 % |
| 5 | **SPY** S&P 500 | +4,5 % | ▲ | 25 % |
| 6 | **QQQ** Nasdaq 100 | +3,9 % | ▽ | — |
| 7 | **EZU** Zone euro | +1,8 % | ▲ | — |
| 8 | **EEM** Marchés émergents | +0,2 % | ▽ | — |

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

- `29/07 17:20` — 4 ordres exécutés
- `29/07 08:46` — Portefeuille déjà aligné — aucun ordre
- `29/07 02:10` — 1 ordre exécuté
- `28/07 18:52` — Portefeuille déjà aligné — aucun ordre
- `28/07 11:49` — Portefeuille déjà aligné — aucun ordre
- `28/07 05:39` — 2 ordres exécutés

---
_Stratégie : momentum 3 & 6 mois, filtre MM100, Top 5 pondéré inverse-volatilité (max 25 %/ligne), bande 4 %, frais 0,10 %/ordre (min 1 €), arbitrage au plus toutes les 6 h. Passage horaire via GitHub Actions._

_Outil pédagogique : aucun argent réel, aucune garantie de performance, pas un conseil en investissement._