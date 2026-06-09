class ContaBancaria:
    def __init__(self, numero, titular, banco, saldo_inicial):
        self.__numero = None
        self.__titular = None
        self.__banco = None
        self.__saldo = 0

        if numero > 0:
            self.__numero = numero

        if titular is not None:
            self.__titular = titular

        if banco is not None:
            self.__banco = banco

        if saldo_inicial >= 0:
            self.__saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False

    def consultar_saldo(self):
        return self.__saldo

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_banco(self):
        return self.__banco

    def esta_ativa(self):
        return self.__saldo > 0
