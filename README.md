Sistema de Cadastro de Clientes

Python | Tkinter | Flask | SQLite

Sobre o Projeto

Este projeto simula um sistema interno corporativo, com foco em manutenção de dados, regras de negócio e organização de código, conceitos comuns em aplicações desktop utilizadas por empresas.

O sistema possui duas versões complementares:

Desktop (Tkinter) — versão principal

Web (Flask) — criada apenas para demonstração no navegador

Tecnologias

Python 3

Tkinter (desktop)

Flask (web)

SQLite

Git / GitHub

Estrutura
sistema-clientes/
├── app/        # Aplicação desktop (Tkinter)
├── web/        # Versão web (Flask)
├── data/       # Banco SQLite
└── README.md


O código é organizado em camadas para facilitar leitura e manutenção:

Regras de negócio

Acesso a dados (SQL)

Interface com o usuário

Funcionalidades

Cadastro de clientes

Listagem de clientes ativos

Exclusão lógica

Validações básicas

Persistência em banco de dados

Executar o Projeto
Desktop (Tkinter)
python -m app.gui

Web (Flask)
python web/app.py


Acesse:

http://127.0.0.1:5000


A versão web existe apenas para fins de demonstração pública.
A aplicação desktop representa o uso principal do sistema.

Banco de Dados

SQLite local

Estrutura simples

Exclusão lógica para preservar histórico

Objetivo

Demonstrar organização, lógica de programação e entendimento de sistemas corporativos, independentemente da tecnologia utilizada.

Observação Final

Embora o projeto utilize Python, os conceitos aplicados são comuns em sistemas internos desenvolvidos com tecnologias como Delphi ou PowerBuilder.
