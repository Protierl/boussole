# 🧭 BOUSSOLE — bot 24h/24

**SIMULATION · cours réels · capital fictif** — mis à jour le 11/11/2026 à 07:31 (Paris) · sources : directes

## 🔴 9 234,27 €

**-765,73 € (-7,7 %)** · jour +0,3 % depuis le 12/07/2026

![Courbe de performance](courbe.png)

| Indicateur | Valeur | Indicateur | Valeur |
|---|---|---|---|
| Perf. annualisée | -21,2 % | Volatilité ann. | 10,5 % |
| Drawdown max | -9,0 % | Sharpe | -1,52 |
| Exposition | 89 % | Liquidités | 1 024,64 € |
| Trades clôturés | 119 (35 % gagnants) | Frais cumulés | 392,30 € |
| EUR/USD | 1,1157 | P&L réalisé | -929,85 € |

## Positions

| Actif | Qté | Cours | Valeur | P&L | Poids |
|---|---|---|---|---|---|
| **AAPL** Apple | 7,558 | 348,51 $ | 2 360,80 € | +3,7 % | 26 % |
| **MSFT** Microsoft | 3,659 | 533,16 $ | 1 748,46 € | +10,7 % | 19 % |
| **AMZN** Amazon | 6,648 | 270,87 $ | 1 614,11 € | +0,8 % | 17 % |
| **META** Meta | 2,301 | 641,39 $ | 1 322,62 € | +0,4 % | 14 % |
| **USO** Pétrole WTI | 9,178 | 141,45 $ | 1 163,65 € | -8,3 % | 13 % |

## Signaux (classement momentum)

| # | Actif | Momentum | Tendance | Cible |
|---|---|---|---|---|
| 1 | **MSFT** Microsoft | +19,4 % | ▲ | 20 % |
| 2 | **AAPL** Apple | +15,4 % | ▲ | 25 % |
| 3 | **USO** Pétrole WTI | +6,4 % | ▲ | 15 % |
| 4 | **META** Meta | +5,9 % | ▲ | 18 % |
| 5 | **JPM** JPMorgan | +4,1 % | ▽ | — |
| 6 | **AMZN** Amazon | +1,2 % | ▲ | 17 % |
| 7 | **DBC** Panier mat. prem. | +0,7 % | ▽ | — |
| 8 | **SPY** S&P 500 | -1,3 % | ▽ | — |

## Derniers ordres

| Date | Sens | Actif | Montant | P&L | Raison |
|---|---|---|---|---|---|
| 10/11 18:53 | VENTE | **DBC** | 2 250,18 € | -128,13 € | Momentum devenu négatif |
| 10/11 18:53 | ACHAT | **AMZN** | 1 600,49 € | — | Entrée momentum · rang 5 |
| 09/11 18:34 | ACHAT | **META** | 1 316,49 € | — | Entrée momentum · rang 4 |
| 05/11 23:01 | VENTE | **JPM** | 2 083,69 € | -85,63 € | Filtre de tendance (< MM100) |
| 05/11 23:01 | ACHAT | **AAPL** | 384,99 € | — | Renforcement vers 25 % |
| 05/11 07:53 | VENTE | **META** | 1 445,87 € | -27,93 € | Filtre de tendance (< MM100) |
| 05/11 07:53 | ACHAT | **JPM** | 2 165,07 € | — | Entrée momentum · rang 4 |
| 04/11 19:00 | VENTE | **MSFT** | 534,50 € | +64,29 € | Allègement vers 19 % |
| 04/11 19:00 | VENTE | **AAPL** | 489,78 € | +22,08 € | Allègement vers 21 % |
| 04/11 19:00 | ACHAT | **META** | 1 470,88 € | — | Entrée momentum · rang 4 |
| 03/11 16:13 | ACHAT | **USO** | 391,90 € | — | Renforcement vers 14 % |
| 03/11 00:35 | VENTE | **SPY** | 2 050,73 € | -27,85 € | Filtre de tendance (< MM100) |

## Journal

- `11/11 07:31` — Portefeuille déjà aligné — aucun ordre
- `10/11 18:53` — 2 ordres exécutés
- `10/11 10:55` — Portefeuille déjà aligné — aucun ordre
- `10/11 02:35` — Portefeuille déjà aligné — aucun ordre
- `09/11 18:34` — 1 ordre exécuté
- `09/11 07:41` — Portefeuille déjà aligné — aucun ordre

---
_Stratégie : momentum 3 & 6 mois, filtre MM100, Top 5 pondéré inverse-volatilité (max 25 %/ligne), bande 4 %, frais 0,10 %/ordre (min 1 €), arbitrage au plus toutes les 6 h. Passage horaire via GitHub Actions._

_Outil pédagogique : aucun argent réel, aucune garantie de performance, pas un conseil en investissement._