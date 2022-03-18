class Pessoa:
    nome = ""
    rg = ""
    endereco = ""
    contato = ""

    def __init__(self, nome, rg, endereco, contato):
        """Definição do construtor da classe Pessoa

        Args:
            nome (String): recebe uma string contendo o nome
            rg (String): recebe uma string contendo rg
            endereco (String): recebe uma string contendo endereço
            contato (String): recebe uma string contendo o contato
        """

        self.nome = nome
        self.rg = rg
        self.endereco = endereco
        self.contato = contato

    # sets e gets usados para retornar ou alterar determinado
    # valor dos atributos

    def get_nome(self):
        try:
            return self.nome
        except Exception as e:
            print(str(e))

    def set_nome(self, nome):
        try:
            self.nome = nome
        except Exception as e:
            print(str(e))

    def get_rg(self):
        try:
            return self.rg
        except Exception as e:
            print(str(e))

    def set_rg(self, rg):
        try:
            self.rg = rg
        except Exception as e:
            print(str(e))

    def get_endereco(self):
        try:
            return self.endereco
        except Exception as e:
            print(str(e))

    def set_endereco(self, endereco):
        try:
            self.endereco = endereco
        except Exception as e:
            print(str(e))

    def get_contato(self):
        try:
            return self.contato
        except Exception as e:
            print(str(e))

    def set_contato(self, contato):
        try:
            self.contato = contato
        except Exception as e:
            print(str(e))
