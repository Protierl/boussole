# 🧭 BOUSSOLE — bot 24h/24

**SIMULATION · cours réels · capital fictif** — mis à jour le 31/07/2026 à 17:30 (Paris) · sources : directes

## 🔴 9 385,32 €

**-614,68 € (-6,1 %)** · jour -1,8 % depuis le 12/07/2026

![Courbe de performance](courbe.png)

| Indicateur | Valeur | Indicateur | Valeur |
|---|---|---|---|
| Perf. annualisée | -70,2 % | Volatilité ann. | 16,1 % |
| Drawdown max | -6,4 % | Sharpe | -5,16 |
| Exposition | 89 % | Liquidités | 1 022,33 € |
| Trades clôturés | 33 (21 % gagnants) | Frais cumulés | 115,85 € |
| EUR/USD | 1,1507 | P&L réalisé | -467,73 € |

## Positions

| Actif | Qté | Cours | Valeur | P&L | Poids |
|---|---|---|---|---|---|
| **JPM** JPMorgan | 7,713 | 353,36 $ | 2 368,60 € | +0,8 % | 25 % |
| **QQQ** Nasdaq 100 | 3,693 | 681,74 $ | 2 187,93 € | -0,2 % | 23 % |
| **AAPL** Apple | 8,263 | 301,93 $ | 2 168,14 € | -7,3 % | 23 % |
| **MSFT** Microsoft | 2,492 | 457,49 $ | 990,71 € | +1,4 % | 11 % |
| **USO** Pétrole WTI | 5,718 | 130,33 $ | 647,61 € | -0,8 % | 7 % |

## Signaux (classement momentum)

| # | Actif | Momentum | Tendance | Cible |
|---|---|---|---|---|
| 1 | **USO** Pétrole WTI | +26,6 % | ▲ | 11 % |
| 2 | **AAPL** Apple | +14,1 % | ▲ | 16 % |
| 3 | **JPM** JPMorgan | +14,1 % | ▲ | 25 % |
| 4 | **MSFT** Microsoft | +8,9 % | ▲ | 12 % |
| 5 | **DBC** Panier mat. prem. | +5,7 % | ▲ | 25 % |
| 6 | **AMZN** Amazon | +5,6 % | ▲ | — |
| 7 | **QQQ** Nasdaq 100 | +5,2 % | ▲ | — |
| 8 | **SPY** S&P 500 | +4,8 % | ▲ | — |

## Derniers ordres

| Date | Sens | Actif | Montant | P&L | Raison |
|---|---|---|---|---|---|
| 31/07 05:56 | VENTE | **DBC** | 2 129,21 € | -26,10 € | Sorti du Top 5 |
| 31/07 05:56 | ACHAT | **MSFT** | 976,20 € | — | Entrée momentum · rang 4 |
| 31/07 05:56 | ACHAT | **AAPL** | 610,49 € | — | Renforcement vers 25 % |
| 30/07 16:34 | VENTE | **SPY** | 2 412,30 € | -34,79 € | Sorti du Top 5 |
| 30/07 16:34 | ACHAT | **QQQ** | 2 189,95 € | — | Entrée momentum · rang 5 |
| 30/07 16:34 | ACHAT | **AAPL** | 705,85 € | — | Renforcement vers 18 % |
| 30/07 16:34 | ACHAT | **DBC** | 552,47 € | — | Renforcement vers 22 % |
| 30/07 16:34 | ACHAT | **JPM** | 492,62 € | — | Renforcement vers 24 % |
| 29/07 17:20 | VENTE | **QQQ** | 1 511,57 € | -32,52 € | Filtre de tendance (< MM100) |
| 29/07 17:20 | VENTE | **EZU** | 1 862,27 € | -24,54 € | Sorti du Top 5 |
| 29/07 17:20 | ACHAT | **DBC** | 1 598,10 € | — | Entrée momentum · rang 4 |
| 29/07 17:20 | ACHAT | **USO** | 651,85 € | — | Entrée momentum · rang 1 |

## Journal

- `31/07 12:00` — Portefeuille déjà aligné — aucun ordre
- `31/07 05:56` — 3 ordres exécutés
- `30/07 22:36` — Portefeuille déjà aligné — aucun ordre
- `30/07 16:34` — 5 ordres exécutés
- `30/07 08:43` — Portefeuille déjà aligné — aucun ordre
- `30/07 00:15` — Portefeuille déjà aligné — aucun ordre

---
_Stratégie : momentum 3 & 6 mois, filtre MM100, Top 5 pondéré inverse-volatilité (max 25 %/ligne), bande 4 %, frais 0,10 %/ordre (min 1 €), arbitrage au plus toutes les 6 h. Passage horaire via GitHub Actions._

_Outil pédagogique : aucun argent réel, aucune garantie de performance, pas un conseil en investissement._