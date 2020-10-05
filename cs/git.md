# Git

https://learngitbranching.js.org/?locale=fr_FR

## HEAD

HEAD est le nom symbolique pour le commit sur lequel nous nous situons actuellement, plus simplement c'est le commit sur lequel nous travaillons.

HEAD pointe toujours sur le commit le plus récent dans l'arbre des commits. La plupart des commandes git qui modifient l'arbre des commits vont commencer par modifier HEAD.

Normalement HEAD pointe sur le nom d'une branche (comme bugFix). Quand vous effectuez un commit, le statut de bugFix est modifié et ce changement est visible par le biais de HEAD.

### HEAD détaché

Détacher HEAD signifie simplement que l'on attache HEAD à un commit au lieu d'une branche.

```
git checkout <commit_hash>
```

## Références relatives

### Opérateur `^`

Revenir d'un commit en arrière avec `^`.

```
git checkout master^
```

`master^` est équivalent à "le premier parent de master".

`master^^` est le grand-parent (ancêtre de seconde génération) de master.

### Opérateur `~`

Revenir de plusieurs en arrière avec `~<num>`

```
git checkout HEAD~4
```

## Forcer les branches

```
git branch -f master HEAD~3
```

Déplace (de force) la branche master à trois parents derrière HEAD.

## Annuler des changements

### git reset

`git reset` annule des changements en déplaçant la référence en arrière dans le temps sur un commit plus ancien.
En ce sens, on peut considérer cela comme une façon de "réécrire l'histoire"; 
`git reset` fait remonter une branche en arrière comme si le(s) commit(s) n'avait jamais eu lieu.

`git reset` est utilisé pour les branches locales, pour les branches distantes il faut utiliser `git revert`.
 
Effacer le commit courant et le commit parent de la branche locale :

```
git reset HEAD~1
# ou
git reset HEAD^
```
 
### git revert

Pour pouvoir annuler des changements et partager ces annulations avec d'autres, nous devons utiliser `git revert`.

Effacer le commit courant de la branche distante : 

```
git revert HEAD
```

## git tag : marquer un commit

Les tags marquent à jamais certains commits comme "milestone" (étape clé) auxquels vous pouvez vous référer comme à des branches.

Encore plus important, il sont définitifs. Vous ne pouvez donc pas rajouter de commit dans un tag : les tags sont un peu comme un pointeur définitif dans l'arbre des commits.

Créer le tag `v1` pour le commit `<commit_hash>`

```
git tag v1 <commit_hash>
```

Si le hash du commit n'est pas précisé, git tag le HEAD.

## git describe

Parce ce que les tags sont de très bonnes références dans le code, git à une commande pour décrire (describe) la différence entre le commit et le tag le plus récent. Cette commande s'appelle git describe !

Git describe peut vous aider lorsque vous vous êtes beaucoup déplacé; cela peut arriver après un git bisect (chercher l'apparition d'un bug).

Git describe s'écrit comme suit :

```
git describe <ref>
```

où `<ref>` est un n'importe quelle chose que git peut résoudre en un commit. Si vous ne spécifiez pas de ref, HEAD est pris par défaut.

Le résultat de la commande ressemble à :

```
<tag>_<numCommits>_g<hash>
```

où `<tag>` est le tag le plus proche dans l'historique, `<numCommits>` le nombre de commits avec le tag, et `<hash>` le hash/identifiant du commit décrit.

## Les parents

Comme le symbole `~`, le symbole `^` accepte un numéro après lui.

Au lieu d'entrer le nombre de générations à remonter (ce que ~ fait), le symbole ^ détermine quel parent est à remonter. Attention, un merge commit a deux parents ce qui peut porter à confusion.

Normalement Git suit le "premier" parent pour un commit/merge, mais avec un numéro suivi de ^ le comportement par défaut est modifié.

Créer une branche en utilisant une réference :

```
# créé la branche `bugWork` à partir du commit parent 
git branch bugWork HEAD~^2~
```

## git fetch

git fetch procède en deux étapes principales, ni plus ni moins. Cela :

* télécharge les commits que le dépôt distant possède mais qui ne sont pas dans le nôtre, puis...
* met à jour nos branches distantes (par exemple, o/master).

git fetch prend en fait notre représentation locale du dépôt distant pour la synchroniser avec ce à quoi le dépôt distant ressemble réellement (à ce moment-là).

Si vous vous rappelez de la précédente leçon, nous avons dit que les branches distantes reflètent l'état du dépôt distant depuis la dernière fois où vous avez parlé à ces branches distantes. git fetch est le moyen de parler à ces branches distantes ! La relation entre git fetch et les branches distantes devrait vous apparaître clairement maintenant.

git fetch contacte le dépôt distant par Internet (via un protocole comme http:// ou git://).

## git pull

