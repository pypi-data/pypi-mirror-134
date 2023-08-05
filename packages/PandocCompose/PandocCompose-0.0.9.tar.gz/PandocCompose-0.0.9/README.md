# Usage

Welcome to the pandoc-compose READ-ME.

You can see this page in :
- [English](#read-me)
- [Français](#lisez-moi)

# READ-ME

## Usage

`pandoc-compose` lets you manage your documentation base by automating conversion of mutiple MarkDown or other formatted text files using Pandoc.

## Dependencies

Pandoc should be already installed on your computer.

## How does it work?

Just like `docker-compose`, when executed, `pandoc-compose` will search for a `pandoc-compose.yml` file either in current working directory or in a specified destination (see [Synopsis](doc/en/DOCUMENTATION.md#synopsis)) and extract configuration from it to
automate the conversion of your document base from any input format to any output format supported by Pandoc.

See [the documentation](doc/en/DOCUMENTATION.md) for more informations on how to use it.


# LISEZ-MOI

## Usage général

`pandoc-compose` vous permet de gérer votre base documentaire en automatisant la conversion depuis différents formats MarkDown ou autre standard de fichier texte supporté par pandoc.

## Pré-requis

Pour fonctionner, ce logiciel a besoin que pandoc soit préalablement installé sur la machine.

## Comment cela fonctionne-t-il ?

Tout comme `docker-compose`, lorsqu'il est exécuté, `pandoc-compose` va d'abord chercher un fichier `pandoc-compose.yml` dans le répertoire courant ou suivant le chemin passé en argument (voir [Synopsis](doc/fr/DOCUMENTATION.md#synopsis)).
Il en extrait la configuration pour automatiser la conversion documentaire d'un format d'entrée vers un format de sortie supporté par pandoc.

Vous trouverez la documentation [ici](doc/fr/DOCUMENTATION.md) pour plus de détail sur comment composer et utiliser le fichier yaml.
