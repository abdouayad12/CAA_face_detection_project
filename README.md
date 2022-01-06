# Projet de détection de visage.
Ce projet sert à implémenter un algorithme pour détecter le nombre d'étudiants absents dans une salle.

## Infos générales
Projet réalisé en **Décembre 2021** comme travail pratique universitaire, Domaine: Systèmes Distribués et Technologies de la Data Science(SDTS), niveau: Master 1. Le but de ce projet et d'exploiter un modèle de détection de visage(Dans notre cas on utilisera la méthode de [Viola&Jones](https://fr.wikipedia.org/wiki/Méthode_de_Viola_et_Jones)) pour détecter le nombre d'étudiants absents dans une salle de cours.

## Contenu du projet
```text
.
├── GUI_detect_faces.py                   <- Contenant l'interface graphique de ce projet ainsi l'appel de la méthode de détection de visage (c'est le fichier "main")
├── detect_faces.py                       <- Contenant la méthode de détection de visage.
├── haarcascade_frontalface_alt.xml       <- Un fichier XML contenant le calcul des caractéristiques du visage.
│
├── Rapport.pdf                           <- Rapport du projet : Définitions, Comparaisons et Analyses des résultats
│
└── README.md                             <- Informations sur ce projet.
```

## Technologies

- **Python** 
- **OpenCV**
- **TKinter**.

## Build
Pour que l'application marche normalement il faut qu'un interpréteur **Python** soit déjà installé sur la machine dans laquelle ce projet va être exécuté. Puis si vous utilisez un **IDE** (Pycharm, Intellij Idea...), il suffit d'importer le projet, ensuite de configurer l'interpréteur Python (choisir le module SDK, exp-> Python 3.9.7), pour ce faire il suffit de suivre les étapes suivantes: File >Project Structure >Modules >module SDK.

### Importation des librairies
Dans ce projet il faut aussi installer des librairies externes tels que OpenCV et Tkinter, pour cela il faut ouvrir le terminal (utilisation des lignes de commande):
```bash
# Il faut s'assurer que la commande PIP est mise à jour 
$ pip install --upgrade pip
# Installation du module OpenCV (de préférence la version Contrib, elle est plus complète que la version standard)
$ pip install opencv-contrib-python
# Installation du module TKinter(généralement il est installé dans la librairie standard de Python)
$ pip install tk

```
