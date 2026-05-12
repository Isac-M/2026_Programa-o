class PlayList:
    def __init__(self, id, nome, descricao):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_descricao(self):
        return self.__descricao

    def set_nome(self, nome):
        self.__nome = nome

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def __str__(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | Descrição: {self.__descricao}"

class Musica:
    def __init__(self, id, titulo, artista, album):
        self.__id = id
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album

    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def get_artista(self):
        return self.__artista

    def get_album(self):
        return self.__album

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_artista(self, artista):
        self.__artista = artista

    def set_album(self, album):
        self.__album = album

    def __str__(self):
        return f"ID: {self.__id} | Título: {self.__titulo} | Artista: {self.__artista} | Álbum: {self.__album}"