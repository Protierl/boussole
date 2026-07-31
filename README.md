# 🧭 BOUSSOLE — bot 24h/24

**SIMULATION · cours réels · capital fictif** — mis à jour le 31/07/2026 à 23:30 (Paris) · sources : directes

## 🔴 9 442,42 €

**-557,58 € (-5,6 %)** · jour -1,2 % depuis le 12/07/2026

![Courbe de performance](courbe.png)

| Indicateur | Valeur | Indicateur | Valeur |
|---|---|---|---|
| Perf. annualisée | -66,0 % | Volatilité ann. | 15,5 % |
| Drawdown max | -5,8 % | Sharpe | -4,86 |
| Exposition | 86 % | Liquidités | 1 308,01 € |
| Trades clôturés | 34 (24 % gagnants) | Frais cumulés | 120,36 € |
| EUR/USD | 1,1527 | P&L réalisé | -457,24 € |

## Positions

| Actif | Qté | Cours | Valeur | P&L | Poids |
|---|---|---|---|---|---|
| **JPM** JPMorgan | 7,713 | 351,79 $ | 2 353,99 € | +0,2 % | 25 % |
| **AAPL** Apple | 8,263 | 308,91 $ | 2 214,42 € | -5,3 % | 23 % |
| **AMZN** Amazon | 5,546 | 271,58 $ | 1 306,63 € | +0,3 % | 14 % |
| **USO** Pétrole WTI | 11,197 | 129,17 $ | 1 254,74 € | -1,0 % | 13 % |
| **MSFT** Microsoft | 2,492 | 464,72 $ | 1 004,63 € | +2,8 % | 11 % |

## Signaux (classement momentum)

| # | Actif | Momentum | Tendance | Cible |
|---|---|---|---|---|
| 1 | **USO** Pétrole WTI | +25,5 % | ▲ | 13 % |
| 2 | **AAPL** Apple | +16,7 % | ▲ | 22 % |
| 3 | **JPM** JPMorgan | +13,6 % | ▲ | 25 % |
| 4 | **MSFT** Microsoft | +10,6 % | ▲ | 14 % |
| 5 | **AMZN** Amazon | +7,4 % | ▲ | 13 % |
| 6 | **QQQ** Nasdaq 100 | +6,2 % | ▲ | — |
| 7 | **SPY** S&P 500 | +5,8 % | ▲ | — |
| 8 | **DBC** Panier mat. prem. | +5,5 % | ▲ | — |

## Derniers ordres

| Date | Sens | Actif | Montant | P&L | Raison |
|---|---|---|---|---|---|
| 31/07 19:54 | VENTE | **QQQ** | 2 204,84 € | +10,49 € | Sorti du Top 5 |
| 31/07 19:54 | ACHAT | **AMZN** | 1 301,24 € | — | Entrée momentum · rang 5 |
| 31/07 19:54 | ACHAT | **USO** | 613,41 € | — | Renforcement vers 13 % |
| 31/07 05:56 | VENTE | **DBC** | 2 129,21 € | -26,10 € | Sorti du Top 5 |
| 31/07 05:56 | ACHAT | **MSFT** | 976,20 € | — | Entrée momentum · rang 4 |
| 31/07 05:56 | ACHAT | **AAPL** | 610,49 € | — | Renforcement vers 25 % |
| 30/07 16:34 | VENTE | **SPY** | 2 412,30 € | -34,79 € | Sorti du Top 5 |
| 30/07 16:34 | ACHAT | **QQQ** | 2 189,95 € | — | Entrée momentum · rang 5 |
| 30/07 16:34 | ACHAT | **AAPL** | 705,85 € | — | Renforcement vers 18 % |
| 30/07 16:34 | ACHAT | **DBC** | 552,47 € | — | Renforcement vers 22 % |
| 30/07 16:34 | ACHAT | **JPM** | 492,62 € | — | Renforcement vers 24 % |
| 29/07 17:20 | VENTE | **QQQ** | 1 511,57 € | -32,52 € | Filtre de tendance (< MM100) |

## Journal

- `31/07 19:54` — 3 ordres exécutés
- `31/07 12:00` — Portefeuille déjà aligné — aucun ordre
- `31/07 05:56` — 3 ordres exécutés
- `30/07 22:36` — Portefeuille déjà aligné — aucun ordre
- `30/07 16:34` — 5 ordres exécutés
- `30/07 08:43` — Portefeuille déjà aligné — aucun ordre

---
_Stratégie : momentum 3 & 6 mois, filtre MM100, Top 5 pondéré inverse-volatilité (max 25 %/ligne), bande 4 %, frais 0,10 %/ordre (min 1 €), arbitrage au plus toutes les 6 h. Passage horaire via GitHub Actions._

_Outil pédagogique : aucun argent réel, aucune garantie de performance, pas un conseil en investissement._