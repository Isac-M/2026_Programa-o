class Pais:
    def __init__(self, nome, populacao, area):
        self.nome = nome
        self.populacao = populacao
        self.area = area

    def densidade_demografica(self):
        return self.populacao / self.area

paises = []

for i in range(10):
    print(f"\nDigite os dados do país {i+1}:")
    nome = input("Nome: ")
    populacao = float(input("População: "))
    area = float(input("Área (km²): "))
    
    pais = Pais(nome, populacao, area)
    paises.append(pais)

maior = paises[0]

for pais in paises:
    if pais.densidade_demografica() > maior.densidade_demografica():
        maior = pais

print("\nPaís com maior densidade demográfica:")
print(f"Nome: {maior.nome}")
print(f"Densidade: {maior.densidade_demografica():.2f} hab/km²")