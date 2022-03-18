from modules.pessoa import Pessoa


class Funcionario(Pessoa):
    id_func = ""
    cargo = ""

    def __init__(self, nome, rg, endereco, contato, id_func, cargo):
        """Construtor da Classe Funcionário, que herda os atributos da classe Pessoa

        Args:
            nome (string): recebe o nome do funcionário
            rg (string): recebe o rg do funcionário
            endereco (string): recebe o endereço do funcionário
            contato (string): recebe o contato do funcionário, podendo ser e-mail ou telefone
            id_func (string): recebe o id do funcionário
            cargo (string): recebe o cargo do funcionário
        """
        super().__init__(nome, rg, endereco, contato)
        self.id_func = id_func
        self.cargo = cargo

    # sets e gets usados para retornar ou alterar determinado valor dos atributos

    def get_id_func(self):
        try:
            return self.id_func
        except Exception as e:
            print(str(e))

    def set_id_func(self, id_func):
        try:
            self.id_func = id_func
        except Exception as e:
            print(str(e))

    def get_cargo(self):
        try:
            return self.cargo
        except Exception as e:
            print(str(e))

    def set_cargo(self, cargo):
        try:
            self.cargo = cargo
        except Exception as e:
            print(str(e))
