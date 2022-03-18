
class Produto:
    id_produto = ""
    nome_produto = ""
    descricao = ""
    valor = ""
    estoque = ""
    
    def __init__(self, id_produto, nome_produto, descricao, valor, estoque):
        """Método construtor da classe Produto

        Args:
            id_produto (string): recebe o id do produto
            nome_produto (string): string com nome do produto
            descricao (string): string com a descriçao do produto
            valor (int): int com o valor unitário do produto
            estoque (int): int com a quantidade do produto em estoque
        """
        
        self.id_produto = id_produto
        self.nome_produto = nome_produto
        self.descricao = descricao
        self.valor = valor
        self.estoque = estoque
        
        
    #sets e gets usados para retornar ou alterar determinado valor dos atributos
    
    def get_id_produto(self): 
        try:
            return self.id_produto
        except Exception as e:
            print(str(e))
    
    def set_id_produto(self, id_produto):
        try:
            self.id_produto = id_produto
        except Exception as e:
            print(str(e))
    
        
    def get_nome_produto(self): 
        try:
            return self.nome_produto
        except Exception as e:
            print(str(e))
    
    def set_nome_produto(self, nome_produto):
        try:
            self.nome_produto = nome_produto
        except Exception as e:
            print(str(e))
        
    
    def get_descricao(self): 
        try:
            return self.descricao
        except Exception as e:
            print(str(e))
    
    def set_descricao(self, descricao):
        try:
            self.descricao = descricao
        except Exception as e:
            print(str(e))
            
            
    def get_valor(self): 
        try:
            return self.valor
        except Exception as e:
            print(str(e))
    
    def set_valor(self, valor):
        try:
            self.valor = valor
        except Exception as e:
            print(str(e))
            

    def get_estoque(self): 
        try:
            return self.estoque
        except Exception as e:
            print(str(e))
    
    def set_estoque(self, estoque):
        try:
            self.estoque = estoque
        except Exception as e:
            print(str(e))