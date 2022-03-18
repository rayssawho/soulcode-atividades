from modules.aluno import Aluno

class Aluno_port(Aluno):
    nota_port = ""
    
    def __init__(self, nome, rg, endereco, contato, matricula, nota_port):
        """Construtor da Classe Aluno_port que herda os atributos da classe Aluno

        Args:
            nome (string): recebe o nome do aluno de português
            rg (string): recebe o numero do rg do aluno de português
            endereco (string): recebe o endereço do aluno de português
            contato (string): recebe o email ou telefone do aluno de português
            matricula (string): recebe o numero da matricula do aluno de português
            nota_port (string): recebe a nota do aluno de português
        """
        super().__init__(nome, rg, endereco, contato, matricula)
        self.nota_port = nota_port
        
     
     #sets e gets usados para retornar ou alterar determinado valor dos atributos    
       
    
    def get_nota_port(self): 
        try:
            return self.nota_port
        except Exception as e:
            print(str(e))
    
    def set_nota_port(self, nota_port):
        try:
            self.nota_port = nota_port
        except Exception as e:
            print(str(e))