class Cliente:
    def __init__(self, nome, cpf, telefone=None, email=None):
        self.__nome = None
        self.__cpf = None
        self.__telefone = None
        self.__email = None

        if self.__validar_nome(nome):
            self.__nome = nome

        if self.__validar_cpf(cpf):
            self.__cpf = self.__limpar_numeros(cpf)

        self.alterar_telefone(telefone)
        self.alterar_email(email)

    def __limpar_numeros(self, texto):
        return ''.join(caractere for caractere in texto if caractere.isdigit())

    def __validar_nome(self, nome):
        return nome is not None and len(nome.strip()) >= 5

    def __validar_cpf(self, cpf):
        if cpf is None:
            return False
        cpf_limpo = self.__limpar_numeros(cpf)
        return len(cpf_limpo) == 11

    def __validar_telefone(self, telefone):
        if telefone is None or telefone == "":
            return True
        telefone_limpo = self.__limpar_numeros(telefone)
        return 10 <= len(telefone_limpo) <= 11

    def __validar_email(self, email):
        if email is None or email == "":
            return True
        return "@" in email

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_telefone(self):
        return self.__telefone

    def get_email(self):
        return self.__email

    def alterar_telefone(self, telefone):
        if self.__validar_telefone(telefone):
            if telefone is not None:
                self.__telefone = self.__limpar_numeros(telefone)

    def alterar_email(self, email):
        if self.__validar_email(email):
            self.__email = email
