from app.database import conectar

def criar_tabela():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        ativo INTEGER DEFAULT 1
        )
        """)
        conn.commit()

def inserir(nome, email):
    with conectar() as conn:
        conn.execute(
            "INSERT INTO clientes (nome, email) VALUES (?, ?)",
            (nome, email)
        )
        conn.commit()

def listar():
    with conectar() as conn:
        cursor = conn.cursor()
        return cursor.execute(
            "SELECT id, nome, email FROM clientes WHERE ativo = 1"
        ).fetchall()

def atualizar(id, nome, email):
    with conectar() as conn:
        conn.execute(
            "UPDATE clientes SET nome = ?, email = ? WHERE id = ?",
            (nome, email, id)
        )
        conn.commit()

def excluir(id):
    with conectar() as conn:
        conn.execute(
            "UPDATE clientes SET ativo = 0 WHERE id = ?",
            (id,)
        )
        conn.commit()