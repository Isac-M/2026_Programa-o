class Frete:
    def _init_(self, distancia, peso):
        self.distancia = distancia
        self.peso = peso
        
for i in range(10):
    print(f"\nDigite a distancia e peso do fretado {i+1}:")
    distancia = float(input("Destino (km²): "))
    peso = float(input("peso (Kg): "))