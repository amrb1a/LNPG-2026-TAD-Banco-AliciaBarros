class Banco:
    def __init__(self, nome, codigo):
        self.__nome = None
        self.__codigo = None
        self.__contas = []

        if self.__validar_nome(nome):
            self.__nome = nome

        if self.__validar_codigo(codigo):
            self.__codigo = codigo

    def __validar_nome(self, nome):
        return nome is not None and len(nome.strip()) >= 3

    def __validar_codigo(self, codigo):
        return codigo > 0

    def adicionar_conta(self, conta):
        if conta is None:
            return False

        if conta.get_banco() != self:
            return False

        if self.buscar_conta(conta.get_numero()) is not None:
            return False

        self.__contas.append(conta)
        return True

    def remover_conta(self, numero):
        conta = self.buscar_conta(numero)

        if conta is not None:
            self.__contas.remove(conta)
            return True

        return False

    def buscar_conta(self, numero):
        for conta in self.__contas:
            if conta.get_numero() == numero:
                return conta
        return None

    def quantidade_contas(self):
        return len(self.__contas)

    def listar_contas(self):
        return self.__contas

    def get_nome(self):
        return self.__nome

    def get_codigo(self):
        return self.__codigo
