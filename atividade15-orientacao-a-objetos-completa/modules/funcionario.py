from modules.pessoa import Pessoa

class Funcionario(Pessoa):
    
    id_func = ""
    valor_vendas = ""
    
    def __init__(self, nome, numero_doc, endereco, telefone, id_func, valor_vendas):
        """Construtor da classe Funcionario

        Args:
            nome (string): Recebe o nome do funcionário
            numero_doc (string): Recebe o número do documento escolhido acima
            endereco (string): Recebe o endereço do funcionário
            telefone (string): Recebe o telefone do funcionário
            valor_vendas (float): valor de vendas realizada pelo funcionário
        """
        super().__init__(nome, numero_doc, endereco, telefone)
        
        self.id_func = id_func
        self.valor_vendas = valor_vendas
     
     
    #sets e gets usados para retornar ou alterar determinado valor dos atributos 
       
    def get_id_func(self):
        try:
            return self.id_func
        except Exception as e:
            print(str(e))
    
    def set_id_func(self):
        try:
            self.id_func = id_func
        except Exception as e:
            print(str(e))
       
    
    
    def get_valor_vendas(self):
        try:
            return self.valor_vendas
        except Exception as e:
            print(str(e))
    
    def set_valor_vendas(self):
        try:
            self.valor_vendas = valor_vendas
        except Exception as e:
            print(str(e))
    