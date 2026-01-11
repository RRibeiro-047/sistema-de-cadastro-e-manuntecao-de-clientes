from flask import Flask, render_template, request, redirect
from database import conectar

app = Flask(__name__)

def criar_tabela():
    with conectar() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                ativo INTEGER DEFAULT 1
            )
        """)
        conn.commit()

@app.route("/")
def index():
    with conectar() as conn:
        clientes = conn.execute(
            "SELECT id, nome, email FROM clientes WHERE ativo = 1"
        ).fetchall()
    return render_template("index.html", clientes=clientes)

@app.route("/add", methods=["POST"])
def add():
    nome = request.form["nome"]
    email = request.form["email"]
    with conectar() as conn:
        conn.execute(
            "INSERT INTO clientes (nome, email) VALUES (?, ?)",
            (nome, email)
        )
        conn.commit()
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    with conectar() as conn:
        conn.execute(
            "UPDATE clientes SET ativo = 0 WHERE id = ?",
            (id,)
        )
        conn.commit()
    return redirect("/")

if __name__ == "__main__":
    criar_tabela()
    app.run(debug=True)
