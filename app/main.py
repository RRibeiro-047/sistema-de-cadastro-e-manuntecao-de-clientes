import os
import time
from app.models import Cliente
from app.repository import (
    criar_tabela,
    inserir,
    listar,
    atualizar,
    excluir,
)


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPressione Enter para continuar...")


def cadastrar_cliente():
    limpar_tela()
    print("--- Cadastrar Novo Cliente ---")
    try:
        nome = input("Nome: ")
        email = input("E-mail: ")
        cliente = Cliente(nome, email)
        inserir(cliente.nome, cliente.email)
        print("\nCliente cadastrado com sucesso!")
    except ValueError as e:
        print(f"\nErro de validação: {e}")
    except Exception as e:
        print(f"\nOcorreu um erro: {e}")
    pausar()


def listar_clientes():
    limpar_tela()
    print("--- Lista de Clientes ---")
    clientes = listar()
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for cliente in clientes:
            print(f"ID: {cliente[0]}, Nome: {cliente[1]}, E-mail: {cliente[2]}")
    pausar()


def atualizar_cliente():
    limpar_tela()
    print("--- Atualizar Cliente ---")
    try:
        id_cliente = int(input("ID do cliente a ser atualizado: "))
        nome = input("Novo nome: ")
        email = input("Novo e-mail: ")
        cliente = Cliente(nome, email)
        atualizar(id_cliente, cliente.nome, cliente.email)
        print("\nCliente atualizado com sucesso!")
    except ValueError as e:
        print(f"\nErro de validação: {e}")
    except Exception as e:
        print(f"\nOcorreu um erro: {e}")
    pausar()


def excluir_cliente():
    limpar_tela()
    print("--- Excluir Cliente ---")
    try:
        id_cliente = int(input("ID do cliente a ser excluído: "))
        excluir(id_cliente)
        print("\nCliente excluído com sucesso!")
    except Exception as e:
        print(f"\nOcorreu um erro: {e}")
    pausar()


def main():
    criar_tabela()
    while True:
        limpar_tela()
        print("--- Sistema de Gestão de Clientes ---")
        print("1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Atualizar Cliente")
        print("4 - Excluir Cliente")
        print("0 - Sair")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            atualizar_cliente()
        elif opcao == "4":
            excluir_cliente()
        elif opcao == "0":
            print("\nSaindo do sistema...")
            time.sleep(1)
            limpar_tela()
            break
        else:
            print("\nOpção inválida! Tente novamente.")
            time.sleep(1)


if __name__ == "__main__":
    main()
