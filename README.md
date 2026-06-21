# Bluck_renammer
# Bulk File Renamer (Python)

## 📌 Description
Ce projet est un script d'automatisation développé en Python. Il permet de parcourir un dossier ciblé, de filtrer les fichiers (par exemple, isoler uniquement les formats d'images), et de les renommer automatiquement en masse selon une nomenclature structurée (ex: `photo_1.jpg`, `photo_2.jpg`, etc.).

## 🚀 Fonctionnalités
* **Ciblage sécurisé** : Utilisation de chemins absolus ou relatifs pour isoler le dossier de travail.
* **Filtrage précis** : Analyse des extensions de fichiers grâce à la bibliothèque native `pathlib`.
* **Indexation automatique** : Intégration d'un compteur dynamique pour éviter l'écrasement des fichiers.
* **Approche Pro** : Conçu avec une logique de simulation ("Dry Run") pour valider les changements avant application.

## 🛠️ Technologies utilisées
* **Python 3.x**
* Module natif : `pathlib` (Gestion des chemins et des flux de fichiers)
