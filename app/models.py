class Cliente:
    def __init__(self, nome: str, email: str):
        if not nome.strip():
            raise ValueError("Nome não pode ser vazio")
        if "@" not in email:
            raise ValueError("E-mail inválido")

        self.nome = nome
        self.email = email
