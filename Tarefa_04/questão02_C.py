class Playlist:
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao

    def __str__(self):
        return f"Playlist: {self.id} - {self.nome} - {self.descricao}"

class Musica:
    def __init__(self, id, titulo, artista, album):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.album = album

    def __str__(self):
        return f"Música: {self.id} - {self.titulo} - {self.artista} - {self.album}"

class PlaylistItem:
    def __init__(self, id, id_playlist, id_musica, sequencia):
        self.id = id
        self.id_playlist = id_playlist
        self.id_musica = id_musica
        self.sequencia = sequencia

    def __str__(self):
        return f"Item: {self.id} - Playlist {self.id_playlist} - Música {self.id_musica} - Seq {self.sequencia}"

class UI:
    playlists = []
    musicas = []
    itens = []

    @staticmethod
    def menu():
        print("\n1 - Inserir Playlist")
        print("2 - Inserir Música")
        print("3 - Inserir Item")
        print("4 - Listar Playlists")
        print("5 - Listar Músicas")
        print("6 - Listar Itens")
        print("0 - Sair")

    @staticmethod
    def inserir_playlist():
        id = int(input("ID: "))
        nome = input("Nome: ")
        descricao = input("Descrição: ")

        p = Playlist(id, nome, descricao)
        UI.playlists.append(p)

    @staticmethod
    def inserir_musica():
        id = int(input("ID: "))
        titulo = input("Título: ")
        artista = input("Artista: ")
        album = input("Álbum: ")

        m = Musica(id, titulo, artista, album)
        UI.musicas.append(m)

    @staticmethod
    def inserir_item():
        id = int(input("ID: "))
        id_playlist = int(input("Playlist: "))
        id_musica = int(input("Música: "))
        sequencia = int(input("Sequência: "))

        item = PlaylistItem(id, id_playlist, id_musica, sequencia)
        UI.itens.append(item)

    @staticmethod
    def listar_playlists():
        for p in UI.playlists:
            print(p)

    @staticmethod
    def listar_musicas():
        for m in UI.musicas:
            print(m)

    @staticmethod
    def listar_itens():
        for i in UI.itens:
            print(i)

    @staticmethod
    def main():
        op = -1

        while op != 0:
            UI.menu()
            op = int(input("Escolha: "))

            if op == 1:
                UI.inserir_playlist()

            elif op == 2:
                UI.inserir_musica()

            elif op == 3:
                UI.inserir_item()

            elif op == 4:
                UI.listar_playlists()

            elif op == 5:
                UI.listar_musicas()

            elif op == 6:
                UI.listar_itens()

UI.main()