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

    def set_nome(self, nome):
        self.__nome = nome

    def set_camisa(self, camisa):
        self.__camisa = camisa

    def set_id_time(self, id_time):
        self.__id_time = id_time

    def __str__(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | Camisa: {self.__camisa} | Time: {self.__id_time}"


class UI:
    times = []
    jogadores = []

    @staticmethod
    def menu():
        print("\n1 - Inserir Time")
        print("2 - Listar Times")
        print("3 - Atualizar Time")
        print("4 - Excluir Time")
        print("5 - Inserir Jogador")
        print("6 - Listar Jogadores")
        print("7 - Atualizar Jogador")
        print("8 - Excluir Jogador")
        print("9 - Listar Jogadores de um Time")
        print("10 - Transferir Jogador")
        print("0 - Sair")

    @staticmethod
    def inserir_time():
        id = int(input("ID: "))
        nome = input("Nome: ")
        estado = input("Estado: ")

        t = Time(id, nome, estado)
        UI.times.append(t)

    @staticmethod
    def listar_times():
        for t in UI.times:
            print(t)

    @staticmethod
    def atualizar_time():
        id = int(input("Informe o ID do time: "))

        for t in UI.times:
            if t.get_id() == id:
                t.set_nome(input("Novo nome: "))
                t.set_estado(input("Novo estado: "))

    @staticmethod
    def excluir_time():
        id = int(input("ID do time: "))

        for t in UI.times:
            if t.get_id() == id:
                UI.times.remove(t)

    @staticmethod
    def inserir_jogador():
        id = int(input("ID: "))
        nome = input("Nome: ")
        camisa = int(input("Camisa: "))
        id_time = int(input("ID do time: "))

        j = Jogador(id, nome, camisa, id_time)
        UI.jogadores.append(j)

    @staticmethod
    def listar_jogadores():
        for j in UI.jogadores:
            print(j)

    @staticmethod
    def atualizar_jogador():
        id = int(input("ID do jogador: "))

        for j in UI.jogadores:
            if j.get_id() == id:
                j.set_nome(input("Novo nome: "))
                j.set_camisa(int(input("Nova camisa: ")))

    @staticmethod
    def excluir_jogador():
        id = int(input("ID do jogador: "))

        for j in UI.jogadores:
            if j.get_id() == id:
                UI.jogadores.remove(j)

    @staticmethod
    def listar_jogadores_do_time():
        id_time = int(input("ID do time: "))

        for j in UI.jogadores:
            if j.get_id_time() == id_time:
                print(j)

    @staticmethod
    def transferir_jogador():
        id_jogador = int(input("ID do jogador: "))
        novo_time = int(input("Novo time: "))

        for j in UI.jogadores:
            if j.get_id() == id_jogador:
                j.set_id_time(novo_time)

    @staticmethod
    def main():
        op = -1

        while op != 0:
            UI.menu()
            op = int(input("Escolha: "))

            if op == 1:
                UI.inserir_time()

            elif op == 2:
                UI.listar_times()

            elif op == 3:
                UI.atualizar_time()

            elif op == 4:
                UI.excluir_time()

            elif op == 5:
                UI.inserir_jogador()

            elif op == 6:
                UI.listar_jogadores()

            elif op == 7:
                UI.atualizar_jogador()

            elif op == 8:
                UI.excluir_jogador()

            elif op == 9:
                UI.listar_jogadores_do_time()

            elif op == 10:
                UI.transferir_jogador()


UI.main()