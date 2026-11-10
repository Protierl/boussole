# 🧭 BOUSSOLE — bot 24h/24

**SIMULATION · cours réels · capital fictif** — mis à jour le 10/11/2026 à 18:53 (Paris) · sources : directes

## 🔴 9 203,09 €

**-796,91 € (-8,0 %)** · jour -0,8 % depuis le 12/07/2026

![Courbe de performance](courbe.png)

| Indicateur | Valeur | Indicateur | Valeur |
|---|---|---|---|
| Perf. annualisée | -22,1 % | Volatilité ann. | 10,6 % |
| Drawdown max | -9,0 % | Sharpe | -1,59 |
| Exposition | 89 % | Liquidités | 1 024,64 € |
| Trades clôturés | 119 (35 % gagnants) | Frais cumulés | 392,30 € |
| EUR/USD | 1,1157 | P&L réalisé | -929,85 € |

## Positions

| Actif | Qté | Cours | Valeur | P&L | Poids |
|---|---|---|---|---|---|
| **AAPL** Apple | 7,558 | 347,53 $ | 2 354,16 € | +3,4 % | 26 % |
| **MSFT** Microsoft | 3,659 | 530,17 $ | 1 738,65 € | +10,1 % | 19 % |
| **AMZN** Amazon | 6,648 | 268,58 $ | 1 600,49 € | -0,1 % | 17 % |
| **META** Meta | 2,301 | 640,53 $ | 1 320,85 € | +0,2 % | 14 % |
| **USO** Pétrole WTI | 9,178 | 141,53 $ | 1 164,30 € | -8,2 % | 13 % |

## Signaux (classement momentum)

| # | Actif | Momentum | Tendance | Cible |
|---|---|---|---|---|
| 1 | **MSFT** Microsoft | +18,8 % | ▲ | 19 % |
| 2 | **AAPL** Apple | +16,4 % | ▲ | 25 % |
| 3 | **META** Meta | +8,4 % | ▲ | 18 % |
| 4 | **USO** Pétrole WTI | +4,6 % | ▲ | 15 % |
| 5 | **JPM** JPMorgan | +3,0 % | ▽ | — |
| 6 | **AMZN** Amazon | +0,8 % | ▲ | 17 % |
| 7 | **DBC** Panier mat. prem. | -0,7 % | ▽ | — |
| 8 | **SPY** S&P 500 | -1,2 % | ▽ | — |

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

- `10/11 18:53` — 2 ordres exécutés
- `10/11 10:55` — Portefeuille déjà aligné — aucun ordre
- `10/11 02:35` — Portefeuille déjà aligné — aucun ordre
- `09/11 18:34` — 1 ordre exécuté
- `09/11 07:41` — Portefeuille déjà aligné — aucun ordre
- `09/11 00:45` — Portefeuille déjà aligné — aucun ordre

---
_Stratégie : momentum 3 & 6 mois, filtre MM100, Top 5 pondéré inverse-volatilité (max 25 %/ligne), bande 4 %, frais 0,10 %/ordre (min 1 €), arbitrage au plus toutes les 6 h. Passage horaire via GitHub Actions._

_Outil pédagogique : aucun argent réel, aucune garantie de performance, pas un conseil en investissement._