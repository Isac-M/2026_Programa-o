class Time:
    def __init__(self, id, nome, estado):
        self.__id = id
        self.__nome = nome
        self.__estado = estado

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_estado(self):
        return self.__estado

    def set_id(self, id):
        self.__id = id

    def set_nome(self, nome):
        self.__nome = nome

    def set_estado(self, estado):
        self.__estado = estado

    def __str__(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | Estado: {self.__estado}"


class Jogador:
    def __init__(self, id, nome, camisa, id_time):
        self.__id = id
        self.__nome = nome
        self.__camisa = camisa
        self.__id_time = id_time

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_camisa(self):
        return self.__camisa

    def get_id_time(self):
        return self.__id_time

    def set_id(self, id):
        self.__id = id

    def set_nome(self, nome):
        self.__nome = nome

    def set_camisa(self, camisa):
        self.__camisa = camisa

    def set_id_time(self, id_time):
        self.__id_time = id_time

    def __str__(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | Camisa: {self.__camisa} | Time: {self.__id_time}"