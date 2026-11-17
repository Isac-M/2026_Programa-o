from models.profissional import Profissional
from dao.dao import DAO
import json

class ProfissionalDAO(DAO):
    def __init__(self):
        super().__init__()
        self.__arquivo = "profissionais.json"
        self.__abrir()

    def abrir(self):
        try:
            arquivo = open(self.__arquivo, mode="r")
            list_dic = json.load(arquivo)
            arquivo.close()

            self.__objetos = []
            for dic in list_dic:
                obj = Profissional.from_json(dic)
                self.__objetos.append(obj)

        except FileNotFoundError:
            pass

    def salvar(self):
        arquivo = open(self.__arquivo, mode="w")
        json.dump(self.__objetos, arquivo,
                  default=Profissional.to_json, indent=2)
        arquivo.close()