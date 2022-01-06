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
