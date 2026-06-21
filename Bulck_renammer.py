import re
from time import sleep
from pathlib import Path as P

dossier_cible = P("C:/Users/BC241/Desktop/Mon_Portefolio/rename-/test")
#ici on filtres les dossiers avec uniquemment l'extension png

compteur = 1
for i in dossier_cible.iterdir():
    
#On recherche les differentes extension avec jpg
    if i.suffix == ".jpg":

#On créer le nouveau fichier et on l'implémente en ajoutant 
       nouveau_file = f"photo_{compteur}.jpg"
       dossier = dossier_cible / nouveau_file
       compteur += 1
       print(i.rename(dossier))