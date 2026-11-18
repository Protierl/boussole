# 🧭 BOUSSOLE — bot 24h/24

**SIMULATION · cours réels · capital fictif** — mis à jour le 18/11/2026 à 15:05 (Paris) · sources : directes

## 🔴 9 125,43 €

**-874,57 € (-8,7 %)** · jour +0,1 % depuis le 12/07/2026

![Courbe de performance](courbe.png)

| Indicateur | Valeur | Indicateur | Valeur |
|---|---|---|---|
| Perf. annualisée | -22,8 % | Volatilité ann. | 10,7 % |
| Drawdown max | -9,1 % | Sharpe | -1,62 |
| Exposition | 75 % | Liquidités | 2 295,92 € |
| Trades clôturés | 129 (35 % gagnants) | Frais cumulés | 422,71 € |
| EUR/USD | 1,0972 | P&L réalisé | -1 076,44 € |

## Positions

| Actif | Qté | Cours | Valeur | P&L | Poids |
|---|---|---|---|---|---|
| **AAPL** Apple | 7,558 | 351,91 $ | 2 424,02 € | +6,4 % | 27 % |
| **MSFT** Microsoft | 4,876 | 506,24 $ | 2 249,76 € | +2,6 % | 25 % |
| **USO** Pétrole WTI | 16,866 | 140,24 $ | 2 155,73 € | -0,1 % | 24 % |

## Signaux (classement momentum)

| # | Actif | Momentum | Tendance | Cible |
|---|---|---|---|---|
| 1 | **AAPL** Apple | +14,7 % | ▲ | 25 % |
| 2 | **MSFT** Microsoft | +12,7 % | ▲ | 25 % |
| 3 | **META** Meta | +7,8 % | ▽ | — |
| 4 | **JPM** JPMorgan | +1,6 % | ▽ | — |
| 5 | **USO** Pétrole WTI | +0,7 % | ▲ | 24 % |
| 6 | **AMZN** Amazon | -1,8 % | ▲ | — |
| 7 | **SPY** S&P 500 | -2,6 % | ▽ | — |
| 8 | **DBC** Panier mat. prem. | -2,6 % | ▽ | — |

## Derniers ordres

| Date | Sens | Actif | Montant | P&L | Raison |
|---|---|---|---|---|---|
| 18/11 15:05 | ACHAT | **USO** | 2 155,73 € | — | Entrée momentum · rang 3 |
| 17/11 05:31 | VENTE | **USO** | 2 176,60 € | -63,53 € | Momentum devenu négatif |
| 16/11 23:09 | VENTE | **JPM** | 2 240,27 € | -52,40 € | Filtre de tendance (< MM100) |
| 16/11 23:09 | VENTE | **META** | 1 493,32 € | -36,12 € | Filtre de tendance (< MM100) |
| 16/11 23:09 | ACHAT | **USO** | 917,00 € | — | Renforcement vers 24 % |
| 16/11 23:09 | ACHAT | **MSFT** | 612,10 € | — | Renforcement vers 25 % |
| 13/11 23:40 | VENTE | **MSFT** | 636,76 € | +43,81 € | Allègement vers 18 % |
| 13/11 23:40 | VENTE | **USO** | 512,90 € | -5,73 € | Allègement vers 14 % |
| 13/11 23:40 | VENTE | **AMZN** | 1 975,41 € | +11,60 € | Sorti du Top 5 |
| 13/11 23:40 | ACHAT | **JPM** | 2 288,14 € | — | Entrée momentum · rang 4 |
| 13/11 23:40 | ACHAT | **META** | 1 526,42 € | — | Entrée momentum · rang 3 |
| 12/11 12:21 | VENTE | **USO** | 461,78 € | -21,71 € | Allègement vers 19 % |

## Journal

- `18/11 15:05` — 1 ordre exécuté
- `17/11 23:55` — Portefeuille déjà aligné — aucun ordre
- `17/11 15:29` — Portefeuille déjà aligné — aucun ordre
- `17/11 05:31` — 1 ordre exécuté
- `16/11 23:09` — 4 ordres exécutés
- `16/11 12:29` — Portefeuille déjà aligné — aucun ordre

---
_Stratégie : momentum 3 & 6 mois, filtre MM100, Top 5 pondéré inverse-volatilité (max 25 %/ligne), bande 4 %, frais 0,10 %/ordre (min 1 €), arbitrage au plus toutes les 6 h. Passage horaire via GitHub Actions._

_Outil pédagogique : aucun argent réel, aucune garantie de performance, pas un conseil en investissement._