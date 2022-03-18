from modules.pessoa import Pessoa

class Aluno(Pessoa):
    matricula = ""
    
    def __init__(self, nome, rg, endereco, contato, matricula):
        """Construtor da classe Aluno, que herda os atributos da classe Pessoa

        Args:
            nome (string): recebe o nome do aluno.
            rg (string): recebe o numero do rg do aluno.
            endereco (string): recebe o endereco do aluno
            contato (string): recebe o email ou o telefone do aluno
            matricula (string): [recebe o numero da matricula do aluno
        """
        super().__init__(nome, rg, endereco, contato)
        self.matricula = matricula
        
    #sets e gets usados para retornar ou alterar determinado valor dos atributos    
        
    def get_matricula(self): 
        try:
            return self.matricula
        except Exception as e:
            print(str(e))
    
    def set_matricula(self, matricula):
        try:
            self.matricula = matricula
        except Exception as e:
            print(str(e))