
class Pessoa:
    nome = ""
    numero_doc = ""
    endereco = ""
    telefone = ""
    
    def __init__(self, nome, numero_doc, endereco, telefone):
        """Construtor da Classe Pessoa

        Args:
            nome (string): Recebe o nome
            numero_doc (string): Recebe o número do documento pessoal
            endereco (string): Recebe o endereço da pessoa
            telefone (string): Recebe o telefone da pessoa
        """
        self.nome = nome
        self.numero_doc = numero_doc
        self.endereco = endereco
        self.telefone = telefone
        
    
    #sets e gets usados para retornar ou alterar determinado valor dos atributos
    
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
    
          
    def get_numero_doc(self):
        try:
            return self.numero_doc
        except Exception as e:
            print(str(e))
            
    def set_numero_doc(self, numero_doc):
        try:
            self.numero_doc = numero_doc
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
    
    
    def get_telefone(self):
        try:
            return self.telefone
        except Exception as e:
            print(str(e))
            
    def set_telefone(self, telefone):
        try:
            self.telefone = telefone
        except Exception as e:
            print(str(e))
    
    