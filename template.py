
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    "src/__init__.py",       # 1. Package initialisation
    "src/helper.py",         # 2. Utilities/fonctions helpers
    "src/prompt.py",         # 3. Gestion des prompts (LLM)
    ".env",                  # 4. Variables d'environnement
    "setup.py",              # 5. Configuration du package
    "app.py",                # 6. Point d'entrée principal
    "research/trials.ipynb", # 7. Notebooks expérimentaux
    "test.py"                # 8. Tests unitaires (à déplacer)
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")




# 🔍 Rôle de Chaque Fichier
# src/__init__.py

# Rend le dossier src importable comme package Python

# Peut contenir des variables/fonctions globales

# src/helper.py

# Centralise les fonctions réutilisables :

# python
# def load_config():
#     """Charge la config depuis .env"""
#     # ...
# src/prompt.py

# Stocke les templates pour LLM (ex: ChatGPT) :

# python
# PROMPT_TEMPLATE = """
# Tu es un assistant médical. Réponds à la question :
# {question}
# """
# .env

# Stocke les secrets/configuration :

# OPENAI_API_KEY=sk-...
# PINECONE_INDEX=medical-index
# setup.py

# Définit les dépendances/métadonnées du projet :

# python
# from setuptools import setup
# setup(
#     name="medibot",
#     install_requires=["openai", "pinecone"],
# )
# app.py

# Point d'entrée de l'application (ex: Flask/Streamlit) :

# python
# from flask import Flask
# app = Flask(__name__)
# research/trials.ipynb

# Notebook Jupyter pour les tests R&D (ex: optimisation de prompts)

# test.py (à déplacer dans tests/)

# Tests unitaires avec pytest/unittest :

# python
# def test_prompt_generation():
#     assert generate_prompt("Hello") == expected_output
