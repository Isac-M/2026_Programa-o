class agua:
    def _init_(self, mes, ano, consumo, conta):
        self.mes = mes
        self.ano = ano
        self.consumo = consumo
        self.conta = conta

    def calcular_conta(self):
        if self.consumo <= 10:
            return 38.00
        elif self.consumo <= 20:
            return 38.00 + (self.consumo - 10)
        else:
            return 38.00 + (10 * 5.00) + (self.consumo - 20) * 6.00
        
mes = input("Digite o mês:")
ano = int(input("Digite o ano:"))
consumo = float(input("Digite o consumo:"))


conta = agua
valor = conta.calcular_conta()

print(f"\nConta de agua - {mes}/{ano}")
print(f"Consumo: {consumo}")
print(F"vALOR A PAGAR: R$ {valor:.2f}")