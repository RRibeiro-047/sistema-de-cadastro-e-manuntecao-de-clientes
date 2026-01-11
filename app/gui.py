import tkinter as tk
from tkinter import messagebox
from app.models import Cliente
from app.repository import criar_tabela, inserir, listar, excluir

criar_tabela()

def cadastrar():
    try:
        nome = entry_nome.get()
        email = entry_email.get()
        Cliente(nome, email)
        inserir(nome, email)
        messagebox.showinfo("Sucesso", "Cliente cadastrado")
        listar_clientes()
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def listar_clientes():
    lista.delete(0, tk.END)
    for c in listar():
        lista.insert(tk.END, f"{c[0]} - {c[1]} ({c[2]})")

def remover():
    try:
        selecionado = lista.get(lista.curselection())
        id_cliente = selecionado.split(" - ")[0]
        excluir(id_cliente)
        listar_clientes()
    except:
        messagebox.showwarning("Atenção", "Selecione um cliente")

root = tk.Tk()
root.title("Sistema de Clientes")
root.geometry("500x400")

tk.Label(root, text="Nome").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Button(root, text="Cadastrar", command=cadastrar).pack(pady=5)
tk.Button(root, text="Remover Selecionado", command=remover).pack(pady=5)

lista = tk.Listbox(root, width=60)
lista.pack(pady=10)

listar_clientes()
root.mainloop()
