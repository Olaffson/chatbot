#!/bin/bash

# Créer l'environnement virtuel
python3 -m venv openai-env

# Activer l'environnement virtuel
source openai-env/bin/activate

# Installer les dépendances requises depuis requirements.txt
pip install -r requirements.txt

chmod +x run_streamlit.sh
