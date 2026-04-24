""" *** À FINIR AVANT LE 15 MAI AFIN D'ÊTRE PRÊTE POUR L'EXAMEN FINAL (21 MAI) *** """
# Importation de datetime(date/heure actuelle), pathlib(utilisateur/chemin), shutil(supp,
#   déplacer, copier, archivage), argparse(arguments), os(pas obligatoire, car fait la même 
#   chose que pathlib) et timedelta(différence de date/heure)
# Consignes(structuré, sécurisé et instructif)
# Exigeances (toutes les librairies importées doivent être utilisées intelligemment)
# Guide (note de cours, internet, ancien projet)
# Astuces (utilisation des fonctions et la documentation dans git hub)
# Pointage (source d'encouragement et motivation à revoir)
# Finalité (rendu : beau visuel et affichage d'informations nécessaires)
# Note : En cas d'accrochage, demandez de l'aide à Gabriel, Walter (si dispo) ou l'intello


# Importations
import os
from pathlib import Path
from datetime import datetime
import shutil
import random # Pour un choix aléatoire

# Variable globale
current_directory = os.getcwd()

# Retourne l'utilisateur actuel
def curent_user() -> str:
    return os.getlogin() 

# Retourne vrai ou faux si le chemin existe ou pas
def is_path_exist(chemin: str) -> bool:
    return os.path.exists(chemin)

# Crée n fichiers avec des extensions aléatoires s'ils n'existent pas (juste pour les tests)
def create_file(n: int) -> list:
    format = ["txt", "docx", "log", "ps1", "py", "csv", "jpg", "pdf", "png", "json", "html","jpeg"]
    all_files = []
    for i in range(1, n + 1):
        name = f"fichier{i}.{random.choice(format)}"
        file = os.path.join(current_directory, name)
        if not is_path_exist(file):
            with open(file, "w", encoding="utf-8", newline="") as f:
                f.write(f"Bienvenue dans le {name} !!! ")
            all_files.append(name)
    return all_files

def create_directory(type: str) -> str:
    directory = os.path.join(current_directory, f"Dossier {type}")
    os.mkdir(directory)
    return directory

# Trie les n fichiers 
def sort_file(n : int) -> None:
    list = create_file(n)
    for file in list:
        if file.suffix in [".jpg", ".png", ".jpeg"]:
            shutil.move(file, create_directory("Image"))
        elif file.suffix in [".ps1", ".py", ".json", ".html"]:
            shutil.move(file, create_directory("Projet"))
        elif file.suffix in [".txt", ".docx"]:
            shutil.move(file, create_directory("Texte"))
        elif file.suffix == ".log":
            shutil.move(file, create_directory("Config"))

# Crée une archive
def create_archive(name: str) -> None:
    archive = os.path.join(current_directory, f"Dossier {name}")
    shutil.make_archive(base_name="Archives", 
                        format="zip",
                        root_dir=archive)
    
    shutil.move(archive, create_directory(f"{name}_archive"))

# Un peu de ménage
def collection_information() -> None:
    all = os.listdir(current_directory)
    for value in all:
        value.