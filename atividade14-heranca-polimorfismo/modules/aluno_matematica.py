from modules.aluno import Aluno


class Aluno_mat(Aluno):
    nota_mat = ""

    def __init__(self, nome, rg, endereco, contato, matricula, nota_mat):
        """
        Construtor da Classe Aluno_mat que herda os 
        atributos da classe Aluno

        Args:
            nome (string): recebe o nome do aluno de matemática
            rg (string): recebe o numero do rg do aluno de matemática
            endereco (string): recebe o endereço do aluno de matemática
            contato (string): recebe o email ou telefone do aluno de matemática
            matricula (string): recebe o numero da matricula do aluno de matemática
            nota_mat (string): recebe a nota do aluno de matemática
        """
        super().__init__(nome, rg, endereco, contato, matricula)
        self.nota_mat = nota_mat

    # sets e gets usados para retornar ou alterar determinado valor dos atributos ahsuahsuahsuahsuhauhsuahsuhauhsuhauhsuah ahahaha

    def get_nota_mat(self):
        try:
            return self.nota_mat
        except Exception as e:
            print(str(e))

    def set_nota_mat(self, nota_mat):
        try:
            self.nota_mat = nota_mat
        except Exception as e:
            print(str(e))
