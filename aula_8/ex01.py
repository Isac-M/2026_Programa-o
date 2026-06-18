import json
class cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.id} - {self.nome}"
    def to_json(self):
        return { "id" : self.id, "nome" : self.nome }
    @staticmethod
    def from_json(dic):
        return cliente(dic["id"], dic["nome"])
    

a = cliente(1, "Douglas Crockford")
b = cliente(2, "Jon Bosak")
c = cliente.from_json({ "id" : 3, "nome" : "Alan Turing"})

lista = [a, b, c]

arquivo = open("cliente.json", mode="w")
json.dump(lista, arquivo, default = cliente.to_json, indent = 2)
arquivo.close()

print(a)
print(b)
print(c)
print(a.__dict__)
print(b.__dict__)
print(c.__dict__)
print(vars(a))
print(vars(b))
print(vars(c))
print(a.to_json())
print(b.to_json())
print(c.to_json())

def abrir():
    arquivo = open("clientes.json", mode="r")
    list_dic = json.load(arquivo)
    for dic in list_dic:
        x = cliente.from_json(dic)
        print(x)

#salvar()
abrir()