import json
import os

# Caminho base para a pasta de conteúdos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(BASE_DIR, 'content')

def carregar_links():
    """Carrega a lista de serviços externos do links.json."""
    filepath = os.path.join(CONTENT_DIR, 'links.json')
    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)
