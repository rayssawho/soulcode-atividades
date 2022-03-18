from modules.pessoa import Pessoa

class Cliente(Pessoa):
    id_cliente = ""
    hist_compras = ""
    data_cadastro = ""
    
    def __init__(self, nome, numero_doc, endereco, telefone, id_cliente, hist_compras, data_cadastro):
        """Construtor da Classe Cliente, que herda os atributos da classe Pessoa

        Args:
            nome (string): Recebe o nome do cliente
            numero_doc (string): Recebe o número do documento 
            endereco (string): Recebe o endereço do cliente
            telefone (string): Recebe o telefone do cliente
            id_cliente (string): recebe uma identificação unica para o cliente
            hist_compras (string): recebe o histórico de compras do cliente
            data_cadastro (string): recebe a data do cadastro no sistema
        """
        super().__init__(nome, numero_doc, endereco, telefone)
        
        self.id_cliente = id_cliente
        self.data_cadastro = data_cadastro
        self.hist_compras = hist_compras
        
    
    #sets e gets usados para retornar ou alterar determinado valor dos atributos    
    
    def get_id_cliente(self):
        try:
            return self.id_cliente
        except Exception as e:
            print(str(e))
    
    def set_id_cliente(self, id_cliente):
        try:
            self.id_cliente = id_cliente
        except Exception as e:
            print(str(e))
    
    
    def get_hist_compras(self):
        try:
            return self.hist_compras
        except Exception as e:
            print(str(e))
    
    def set_hist_compras(self, hist_compras):
        try:
            self.hist_compras = hist_compras
        except Exception as e:
            print(str(e))
    
    
        
    def get_data_cadastro(self):
        try:
            return self.data_cadastro
        except Exception as e:
            print(str(e))
    
    def set_data_cadastro(self, data_cadastro):
        try:
            self.data_cadastro = data_cadastro
        except Exception as e:
            print(str(e))
    
    
    