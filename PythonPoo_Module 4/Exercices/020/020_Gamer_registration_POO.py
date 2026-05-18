class Gamer:
    def __init__(self, nome, apelido, jogos_favoritos):
        self.nome = nome
        self.apelido = apelido
        self.jogos_favoritos = jogos_favoritos

    def exibir_perfil(self):
        print("Perfil do Gamer")
        print("Nome:", self.nome)
        print("Apelido:", self.apelido)
        print("Jogos Favoritos:", ", ".join(self.jogos_favoritos))


# Criando um objeto da classe
gamer1 = Gamer(
    "Carlos",
    "ShadowPlayer",
    ["CS2", "Valorant", "League of Legends"]
)

# Exibindo o perfil
gamer1.exibir_perfil()