# Lexique

## A

### Abstraction vs encapsulation

https://stackoverflow.com/questions/15176356/difference-between-encapsulation-and-abstraction

## B

### Bit de poids fort

[Bit de poids fort — Wikipédia](https://fr.wikipedia.org/wiki/Bit_de_poids_fort)

### Bit complément

#### Complément à un

[Complément à un — Wikipédia](https://fr.wikipedia.org/wiki/Compl%C3%A9ment_%C3%A0_un)

* Concerne un nombre binaire
* Inverser tous les bits de ce nombre binaire (permuter les 0 par des 1 et inversement)

#### Complément à deux

[Complément à deux — Wikipédia](https://fr.wikipedia.org/wiki/Compl%C3%A9ment_%C3%A0_deux)

* Le complément à un d’un nombre se comporte alors comme le négatif du nombre original dans certaines opérations arithmétiques. 

## C

### cgroups

[Autour des conteneurs : Qu’est-ce qu’un conteneur ? - Publicis Sapient Engineering - Engineering Done Right](https://blog.engineering.publicissapient.fr/2020/02/24/autour-des-conteneurs-quest-ce-quun-conteneur/)

Les groupes de contrôle constituent une autre fonctionnalité du noyau qui isole et gère les ressources du système.

Ces groupes ont plusieurs fonctions.

#### La priorisation

Les accès Entrées/Sorties (/I/O/), CPU sont partagés par tous les processus du système.
Ce partage n’est pas égalitaire; ainsi un groupe peut recevoir une plus grande part de ces ressources. Il aura donc une priorité plus élevée.

#### La limitation de ressources

Un groupe de processus peut se voir affecter une limite d’utilisation des ressources à ne pas dépasser (cache disque, CPU ou encore mémoire). Si limite il y a, les groupes de contrôles assurent également la compatibilité.

#### La comptabilité

Il s’agit de mesurer pour chaque groupe de processus les quantités de ressources consommées.
Ainsi, si cette mesure vient à s’avérer être supérieure au quota alloué, le groupe de contrôle peut être amené à utiliser le contrôle.

#### Le contrôle

Il s’agit de la possibilité de suspendre, arrêter ou redémarrer un processus. Si vous remontez un peu plus sur la BD, vous verrez que les deux amis du kernel dans la dernière bulle s’appellent /CPU Throttler/ et /OOM Killer/. Il s’agit de deux fonctionnements internes du noyau Linux qui consistent à ne plus donner d’accès au CPU à un process (qui aura donc l’impression de ralentir) ou encore même de le tuer s’il consomme trop de mémoire.
Voilà, on sait maintenant ce que sont les conteneurs et comment ils sont mis en œuvre.
En revanche, il reste un point à préciser et qui ne vous a peut-être pas échappé à la lecture du premier schéma : c’est le container runtime.

### Container runtime

[Autour des conteneurs : Qu’est-ce qu’un conteneur ? - Publicis Sapient Engineering - Engineering Done Right](https://blog.engineering.publicissapient.fr/2020/02/24/autour-des-conteneurs-quest-ce-quun-conteneur/)

Bien que l’exécution d’un conteneur repose sur des mécanismes d’isolation, il n’est pas nécessaire de se préoccuper soi-même de leur gestion pour exécuter un conteneur. Et heureusement, car s’il fallait prendre en charge les appels système pour créer une interface réseau, créer un point de montage à chaque fois que l’on souhaite exécuter quelque chose, cela serait de suite beaucoup plus compliqué.
Les différentes initialisations seront prises en charge et abstraites par l’environnement d’exécution des conteneurs (/container runtime/), qui devra être installé sur la machine hôte.
Disposer d’un environnement d’exécution de conteneurs est donc le seul prérequis à l’exécution de conteneurs.
Et c’est donc lui qui va assurer la portabilité de notre conteneur, en s’assurant que les différentes initialisations soient correctement réalisées selon le système hôte sur lequel il s’exécute.
Nous reviendrons plus en détail sur cette notion dans un futur article.

### CPU bound
https://stackoverflow.com/questions/868568/what-do-the-terms-cpu-bound-and-i-o-bound-mean

## H

### HTTP3

[Comprendre HTTP3 en 5 minutes - Je suis un dev](https://www.jesuisundev.com/comprendre-http3-en-5-minutes/)

## M

### Micro service 

* https://martinfowler.com/articles/microservices.html
* https://microservices.io/patterns/decomposition/decompose-by-subdomain.html

### Mojibrake


### Multiplexage

[Multiplexage — Wikipédia](https://fr.wikipedia.org/wiki/Multiplexage)

## N

### namespaces

[Autour des conteneurs : Qu’est-ce qu’un conteneur ? - Publicis Sapient Engineering - Engineering Done Right](https://blog.engineering.publicissapient.fr/2020/02/24/autour-des-conteneurs-quest-ce-quun-conteneur/)

Un espace de noms est une fonction du système d’exploitation qui permet le partage de ressources globales comme le réseau ou le disque. Les ressources associées à un espace de nom ne seront visibles que par les processus qui ont accès à cet espace de nom.
Les espaces de noms sont au nombre de 7 au sein d’un système Linux et pour les connaître, rien de mieux que la commande : `man unshare`

#### L’espace de nom des points de montage (**mount namespace**)

Mounting and unmounting filesystems will not affect the rest of the filesystem, except for filesystems which are explicitly marked as shared/

Ici, cela va permettre à notre conteneur de pouvoir monter et démonter des systèmes de fichiers, sans que cela n’affecte le reste du système. Dans notre cas, un conteneur est également sujet à la notion de chroot, ou changement de racine, qui permet de lui faire croire que le point de montage qu’on lui donne est la racine du système.

#### L’espace de nom réseau (**network namespace**)

The process will have independent IPv4 and IPv6 stacks, IP routing tables, firewall rules./

Cela permet à chaque conteneur de disposer librement de sa stack réseau. Ainsi, plusieurs conteneurs peuvent écouter sur le même port sur un même système hôte (ce qui est totalement impossible dans un environnement non conteneurisé).

#### L’espace de nom des identifiants de processus (**PID namespace**)

Children will have a distinct set of PID-to-process mappings from their parent/

Le processus exécuté au sein du conteneur aura donc le PID 1 (qui est le premier processus s’exécutant sur une machine) et chacun de ses enfants aura un ID totalement décoléré de ceux du système hôte.

#### L’espace de nom Utilisateur (**user namespace**)

The process will have a distinct set of UIDs, GIDs and capabilities/

Ici encore, l’ensemble des droits à l’intérieur du conteneur seront décolérés de ceux du système hôte.
Ce point peut d’ailleurs donner lieu à quelques points de complexité, sur lesquels nous reviendrons dans un futur article.

#### L’espace de nom UTS (**Unix Timesharing System**)

Setting hostname and domain name will not affect the rest of the system./

Notre processus/conteneur pourra donc changer le nom du système à sa guise.

#### L’espace de nom des communications inter processus (**InterProcess Communication**ou**IPC namespace**)

The process will have an independent namespace for POSIX message queues as well as System V messages queues, semaphore sets and shared memory segments./

Cet espace de noms permet d’isoler la communication au sein des groupes de processus. Ainsi, plusieurs groupes qui appartiennent à des espaces de noms différents pourront se servir de moyens de communications ayant le même nom, sans pour autant entrer en conflit ni avoir d’interférences.

#### L’espace de nom des groupes de contrôle (**Control Groups** ou **CGroups namespace**)

The process will have a virtualized view of procself/cgroup, and new cgroup mounts will be rooted at the namespace cgroup root./

Ici, il s’agit de fournir au processus une vue virtuelle de la notion des groupes de contrôles. Mais qu’est-ce qu’un groupe de contrôle ?
Et bien, c’est tout simplement le deuxième mécanisme qui va nous intéresser. Pour le moment, nous avons vu que le noyau de notre système dispose de moyens pour isoler les différents groupes de processus. En revanche, nous n’avons rien vu qui permette de limiter la consommation des ressources physiques.
S’il y avait uniquement les espaces de noms, un seul processus pourrait utiliser l’ensemble du disque ou encore monopoliser la mémoire vive. C’est là qu’interviennent les cgroups.

### Name mangling

[Name mangling - Wikipedia](https://en.wikipedia.org/wiki/Name_mangling)

## O

### Opération bit à bit

[Opération bit à bit — Wikipédia](https://fr.wikipedia.org/wiki/Op%C3%A9ration_bit_%C3%A0_bit)

## T

### Terraform

[Comprendre Terraform (infra-as-code) en 5 minutes - Je suis un dev](https://www.jesuisundev.com/comprendre-terraform-en-5-minutes/)

Infra As Code

Terraform est un outil d’infrastructure en tant que code.*C’est open source et écrit en  [Go](https://www.jesuisundev.com/comprendre-go-en-5-minutes/)  par  [Hashicorp](https://www.hashicorp.com/) . Concrètement, ça te permet de déclarer, via ton code, ce que tu veux pour ton infrastructure. Dans des fichiers de configuration structurés tu vas pouvoir manager automatiquement ton infrastructure sans action manuelle. *Que ça soit l’approvisionnement initial, la mise à jour ou la destruction de ton infrastructure, c’est le code qui pilote.* 
Dans le monde de l’infra-as-code tu as plusieurs manières de faire les choses. *Terraform opte pour la façon de faire dite déclarative.* Tu déclares dans tes fichiers de configs l’état désiré de ton infrastructure. Terraform ne va ne faire qu’exécuter le minimum pour arriver à l’état que tu désires. 

*Exemple* : ton infrastructure en live a déjà un serveur web et une base de données qui tournent. Ta config dans ton code correspond parfaitement à ça. Tu ajoutes dans ta configuration Terraform que finalement tu veux deux bases de données. Quand tu commit, Terraform va créer une base de données en plus et rien faire d’autre. *Il a atteint l’état désiré déclaré par ton code.* C’est de toute beauté.