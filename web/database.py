import sqlite3
from pathlib import Path

DB_PATH = Path("data/clientes.db")

def conectar():
    return sqlite3.connect(DB_PATH)
