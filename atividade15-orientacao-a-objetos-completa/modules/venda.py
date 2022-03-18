
class Venda:
    id_venda = ""
    produto_id = ""
    cliente_id = ""
    func_id = ""
    venda_valor = ""
    quant_produto = ""
    def __init__(self, id_venda, produto_id, cliente_id, func_id, venda_valor, quant_produto):
        """construtor da Classe Venda

        Args:
            id_venda (string)
            produto_id (string)
            cliente_id (string)
            func_id (string)
            venda_valor (string)
            quant_produto (int)
        """
        
        self.id_venda = id_venda
        self.produto_id = produto_id
        self.cliente_id = cliente_id
        self.func_id = func_id
        self.venda_valor = venda_valor
        self.quant_produto = quant_produto
        
    def get_id_venda(self): 
        try:
            return self.id_venda
        except Exception as e:
            print(str(e))
    
    def set_id_venda(self, id_venda):
        try:
            self.id_venda = id_venda
        except Exception as e:
            print(str(e))
            
    
    def get_produto_id(self): 
        try:
            return self.produto_id
        except Exception as e:
            print(str(e))
    
    def set_produto_id(self, produto_id):
        try:
            self.produto_id = produto_id
        except Exception as e:
            print(str(e))
        
    
    def get_cliente_id(self): 
        try:
            return self.cliente_id
        except Exception as e:
            print(str(e))
    
    def set_cliente_id(self, cliente_id):
        try:
            self.cliente_id = cliente_id
        except Exception as e:
            print(str(e))
        
        
    def get_func_id(self): 
        try:
            return self.func_id
        except Exception as e:
            print(str(e))
    
    def set_func_id(self, func_id):
        try:
            self.func_id = func_id
        except Exception as e:
            print(str(e))
            
            
    def get_venda_valor(self): 
        try:
            return self.venda_valor
        except Exception as e:
            print(str(e))
    
    def set_venda_valor(self, venda_valor):
        try:
            self.venda_valor = venda_valor
        except Exception as e:
            print(str(e))
            
    
    def get_quant_produto(self): 
        try:
            return self.quant_produto
        except Exception as e:
            print(str(e))
    
    def set_quant_produto(self, quant_produto):
        try:
            self.quant_produto = quant_produto
        except Exception as e:
            print(str(e))