*Ceci n'est qu'un brouillon, il y a encore beaucoup de choses à modifier*

# Introduction :

## Le rap en France :
Dès son émergence en tant que genre, le rap s’est plutôt imposé en tant que style engagé, aux paroles scandées et au rythme martelé, que l’on apparente parfois au SLAM. Au fil des années, et notamment dans les années fin 90, le rap a évolué vers une toute autre thématique qui le plus souvent, fait la promotion de **la violence, des crimes et des actes à caractère illégal**. Le plus souvent considéré comme un style banlieusard et est fréquemment associé aux classes populaires. De nos jours, le rap est souvent associé à **la violence, aux crimes et aux illégalités**. Le lexique utilisé au sein des paroles de rap est issu du vocabulaire argotique, informel, souvent considéré comme altéré par les plus puristes d’entre nous. 

## Le RnB en France :
 
D’abord populaire, le RnB  est un genre musical né aux États-Unis dans les années 80. Il est né d’un mélange de rhythm and blues, de hip-hop, de soul et de funk. Il s’imposera comme genre musical prédominant sur la scène internationale dans les années 2000. Le RnB se situe à la confluence du hip-hop et du RnB, puisque des artistes issus des deux genre peuvent collaborer ensemble. De ce fait, les paroles peuvent avoir des styles d’écriture et des thématiques similaires. Le RnB des années 2000 et 2010 voire après, traite le plus souvent de thématiques amoureuses, liées aux relations de couple, à la tromperie, la nostalgie de l’être aimé ou encore la drague et le flirt.  

## Objectifs du projet :

Nous avons choisi de travailler sur un corpus de musiques de rap et de RnB contemporain français. Chaque artiste a une plume qui lui est propre, parfois reconnaissable à l’écrit.  Ainsi, l’objectif de notre projet serait d’établir une étiquette par artiste, afin que le système puisse associer la musique à son étiquette (=artiste).


**Il faut tester au moins deux des algorithmes suivants**

# J48
En utilisant une **cross-validation** sur 10 folds: 
- Documents classifiés correctement: 323 (77%)
- Documents mal cassifiés: 95 (22%)

- Meilleur F-mesure: Aya Nakamura
- Moins bonne F-mesure: Booba


# Naive Bayes
En utilisant une **cross-validation** sur 10 folds: 
- Documents classifiés correctement: 351 (84%)
- Documents mal cassifiés: 66 (15%)

- Meilleur F-mesure: JUL
- Moins bonne F-mesure: Booba


# SVM
En utilisant une **cross-validation** sur 10 folds: 
- Documents classifiés correctement: 349 (83%)
- Documents mal cassifiés: 69 (16%)

- Meilleur F-mesure: JUL
- Moins bonne F-mesure: Booba



# Hypothèses
Je pense que si les résultats sont aussi bon, c'est sûrement parce que quand l'artiste fait une collaboration, les paroles indiquent qui chante, donc le nom de l'artiste est écrit dans le document (oups)
Après, Aya Nakamura dit son nom dans pratiquement toutes ses chansons mais le classifieurs n'est pas parfait non plus.

Est-il nécessaire d'essayer d'autres manières de séparer le corpus ? Avec 418 documents, est-ce qu'on a besoin de faire un train/test ?


# Axes d'amélioration
- Essayer de retirer le nom des artistes dans les musiques en contenant plusieurs pour observer des changements
