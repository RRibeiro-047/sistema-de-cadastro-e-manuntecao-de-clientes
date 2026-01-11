import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent
DATA_DIR = ROOT_PATH / 'data'
DATA_DIR.mkdir(exist_ok=True)
DB_FILE = DATA_DIR / 'clientes.db'

def conectar():
    """Conecta ao banco de dados SQLite."""
    return sqlite3.connect(DB_FILE)