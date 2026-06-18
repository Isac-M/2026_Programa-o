from datetime import datetime

class Pagamento():
    EmAberto = 1
    PagoParcial = 2
    Pago = 3


class Boleto:
    def __init__(self, cod, emissao, venc, valor):
        self.set_cod(cod)
        self.set_emissao(emissao)
        self.set_vencimento(venc)
        self.set_valor(valor)
        self.__valorPago = 0
        self.__situacaoPagamento = Pagamento.EmAberto

    def set_cod(self, cod):
        if cod == "":
            raise ValueError("Código de barras inválido")
        self.__codBarras = cod

    def set_emissao(self, emissao):
        self.__emissao = emissao

    def set_vencimento(self, venc):
        self.__vencimento = venc

    def set_valor(self, valor):
        if valor <= 0:
            raise ValueError("Valor inválido")
        self.__valor = valor

    def get_cod(self):
        return self.__cod

    def get_emissao(self):
        return self.__emissao

    def get_vencimento(self):
        return self.__vencimento

    def get_valor(self):
        return self.__valor

    def get_valorPago(self):
        return self.__valorPago

    def pagar(self, valorPago):
        if valorPago <= 0:
            raise ValueError("Pagamento inválido")

        if self.__valorPago + valorPago > self.__valor:
            raise ValueError("Pagamento maior que o valor do boleto")

        self.__valorPago += valorPago

        if self.__valorPago == 0:
            self.__situacaoPagamento = Pagamento.EmAberto

        elif self.__valorPago < self.__valor:
            self.__situacaoPagamento = Pagamento.PagoParcial

        else:
            self.__situacaoPagamento = Pagamento.Pago

    def situacao(self):
        return self.__situacaoPagamento

    def __str__(self):
        return f"{self.__cod} - {self.__valor} - {self.__valorPago} - {self.situacao().name}"


class BoletoUI:
    __boletos = []

    @staticmethod
    def main():
        op = 0

        while op != 8:
            op = BoletoUI.menu()

            if op == 1:
                BoletoUI.inserir()

            elif op == 2:
                BoletoUI.listar()

            elif op == 3:
                BoletoUI.atualizar()

            elif op == 4:
                BoletoUI.excluir()

            elif op == 5:
                BoletoUI.boletosEmAberto()

            elif op == 6:
                BoletoUI.boletosPagos()

            elif op == 7:
                BoletoUI.pagarBoleto()

    @staticmethod
    def menu():
        print("\n1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir")
        print("5-Boletos em aberto, 6-Boletos pagos")
        print("7-Pagar boleto, 8-Sair")

        return int(input("Informe uma opção: "))

    @classmethod
    def inserir(cls):
        cod = input("Informe o código de barras: ")

        emissao = datetime.strptime(
            input("Informe a data de emissão: "),
            "%d/%m/%Y"
        )

        venc = datetime.strptime(
            input("Informe a data de vencimento: "),
            "%d/%m/%Y"
        )

        valor = float(input("Informe o valor do boleto: "))

        x = Boleto(cod, emissao, venc, valor)

        cls.__boletos.append(x)

    @classmethod
    def listar(cls):
        for x in cls.__boletos:
            print(x)

    @classmethod
    def atualizar(cls):
        cod = input("Informe o código do boleto: ")

        for x in cls.__boletos:
            if x.get_cod() == cod:

                novoValor = float(
                    input("Informe o novo valor: ")
                )

                x.set_valor(novoValor)

                print("Boleto atualizado")
                return

        print("Boleto não encontrado")

    @classmethod
    def excluir(cls):
        cod = input("Informe o código do boleto: ")

        for x in cls.__boletos:
            if x.get_cod() == cod:
                cls.__boletos.remove(x)

                print("Boleto removido")
                return

        print("Boleto não encontrado")

    @classmethod
    def boletosEmAberto(cls):
        for x in cls.__boletos:
            if x.situacao() != Pagamento.Pago:
                print(x)

    @classmethod
    def boletosPagos(cls):
        for x in cls.__boletos:
            if x.situacao() == Pagamento.Pago:
                print(x)

    @classmethod
    def pagarBoleto(cls):
        cod = input("Informe o código do boleto: ")

        for x in cls.__boletos:
            if x.get_codBarras() == cod:

                valor = float(
                    input("Informe o valor do pagamento: ")
                )

                x.pagar(valor)

                print("Pagamento realizado")
                return

        print("Boleto não encontrado")


BoletoUI.main()