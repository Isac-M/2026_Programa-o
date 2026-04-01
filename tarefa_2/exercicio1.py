class Agua:
    def __init__(self, mes, ano, consumo):
        self.mes = mes
        self.ano = ano
        self.consumo = consumo  # em m³

    def calcular_conta(self):
        if self.consumo <= 10:
            return 38.00
        elif self.consumo <= 20:
            return 38.00 + (self.consumo - 10) * 5.00
        else:
            return 38.00 + (10 * 5.00) + (self.consumo - 20) * 6.00


# Programa principal
mes = input("Digite o mês: ")
ano = int(input("Digite o ano: "))
consumo = float(input("Digite o consumo em m³: "))

conta = Agua(mes, ano, consumo)
valor = conta.calcular_conta()

print(f"\nConta de água - {mes}/{ano}")
print(f"Consumo: {consumo} m³")
print(f"Valor a pagar: R$ {valor:.2f}")