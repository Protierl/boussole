# 🧭 BOUSSOLE 24h/24 — installation (5 minutes, depuis l'iPhone)

Le bot tourne **gratuitement** sur GitHub Actions : toutes les heures, GitHub prête une
machine ~1 minute, le bot récupère les cours réels, arbitre si nécessaire, puis publie son
tableau de bord (valeur, courbe, positions, journal) sur la page d'accueil du dépôt.
Aucun serveur, aucune carte bancaire, rien à laisser allumé.

## Étape 1 — Compte GitHub
Sur **github.com** : *Sign up* (gratuit). Si vous avez déjà un compte, passez à l'étape 2.

## Étape 2 — Créer le dépôt
1. Touchez **+** (en haut) → **New repository**.
2. Repository name : `boussole`.
3. Visibilité : **Public** (nécessaire pour que GitHub Actions soit illimité et gratuit).
4. **Create repository**.

> Un dépôt public est visible par tous : n'y mettez rien de personnel. Il n'y a ici que
> le bot et son portefeuille fictif.

## Étape 3 — Ajouter les 2 fichiers
Sur la page du dépôt :

**Fichier 1 :**
1. **Add file → Create new file** (si le dépôt est vide : lien *creating a new file*).
2. Nom du fichier : `bot.py`
3. Collez tout le contenu du fichier **bot.py** fourni par Claude.
4. **Commit changes** (bouton vert), puis confirmez.

**Fichier 2 :**
1. **Add file → Create new file**.
2. Nom du fichier : `.github/workflows/boussole.yml`
   *(tapez le nom tel quel, avec les `/` : GitHub crée les dossiers automatiquement).*
3. Collez tout le contenu du fichier **boussole.yml** fourni par Claude.
4. **Commit changes**.

## Étape 4 — Premier lancement
1. Ouvrez l'onglet **Actions** du dépôt (si un bouton vert propose d'activer les
   workflows, touchez-le).
2. Dans la liste à gauche : **BOUSSOLE 24h/24** → bouton **Run workflow** → **Run workflow**.
3. Attendez ~1 minute, puis revenez à l'accueil du dépôt (onglet **Code**) :
   le tableau de bord est là, avec les premiers achats du bot. 🎉

Ensuite, plus rien à faire : le bot passe **toutes les heures** (à h:17, heure UTC —
l'heure exacte peut glisser de quelques minutes selon la charge de GitHub, c'est normal).

## Consulter le bot
- La page d'accueil du dépôt **est** le tableau de bord (elle se met à jour à chaque cycle).
- Conseil : installez l'app **GitHub** (App Store) et épinglez le dépôt — idéal sur iPhone.
- `etat.json` contient toute la comptabilité (positions, ordres, historique).

## Suivre en direct dans l'app BOUSSOLE
L'app BOUSSOLE (l'artifact Claude) peut afficher ce bot en temps réel :
1. Ouvrez l'app → carte **« Suivre le bot 24h/24 »** (sur l'accueil, ou dans l'onglet *Stratégie*).
2. Collez `votre-utilisateur/boussole` (ou l'adresse complète du dépôt) → **Connecter**.
3. L'app relit l'état publié par le bot toutes les 2 minutes et **revalorise ses positions
   avec des cours en direct** entre deux passages. Un sélecteur permet de basculer entre
   le bot 24h/24 et un bot local d'essai.

> Si vous aviez installé une version antérieure de `bot.py`, remplacez son contenu sur
> GitHub par la dernière version (elle publie aussi les signaux, affichés dans l'app).

## Régler / arrêter
- **Fréquence** : dans `.github/workflows/boussole.yml`, ligne `cron`.
  Exemples : `"*/30 13-21 * * 1-5"` = toutes les 30 min pendant les heures de bourse US,
  `"17 */2 * * *"` = toutes les 2 heures. (Inutile d'aller plus vite que 30 min : la
  stratégie n'arbitre au plus qu'une fois toutes les 6 h.)
- **Pause** : onglet Actions → *BOUSSOLE 24h/24* → menu **⋯** → *Disable workflow*.
- **Repartir de 10 000 €** : supprimez le fichier `etat.json` du dépôt (⋯ → Delete file).
- Si GitHub suspend le planning après une longue inactivité du compte, un simple
  passage sur l'onglet Actions → *Enable* le relance.

## À savoir
- Simulation pédagogique : capital fictif, ordres simulés au dernier cours, aucune
  garantie de performance, pas un conseil en investissement.
- Sources de cours : Yahoo Finance, avec secours automatique (Stooq, puis dernier
  cours connu). En cas de panne totale, le bot reporte l'arbitrage et le note au journal.
- Coût : 0 €. Un cycle ≈ 1 minute de machine ; GitHub l'offre sans limite aux dépôts publics.
