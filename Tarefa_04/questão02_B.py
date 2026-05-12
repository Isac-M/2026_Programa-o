class PlayListItem:
    def __init__(self, id, id_playlist, id_musica, sequencia):
        self.__id = id
        self.__id_playlist = id_playlist
        self.__id_musica = id_musica
        self.__sequencia = sequencia

    def get_id(self):
        return self.__id

    def get_id_playlist(self):
        return self.__id_playlist

    def get_id_musica(self):
        return self.__id_musica

    def get_sequencia(self):
        return self.__sequencia

    def set_id_playlist(self, id_playlist):
        self.__id_playlist = id_playlist

    def set_id_musica(self, id_musica):
        self.__id_musica = id_musica

    def set_sequencia(self, sequencia):
        self.__sequencia = sequencia

    def __str__(self):
        return f"ID: {self.__id} | Playlist: {self.__id_playlist} | Música: {self.__id_musica} | Sequência: {self.__sequencia}"