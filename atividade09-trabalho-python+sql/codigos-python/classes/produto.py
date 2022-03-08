
class produto:
    idproduto = "",
    idfornecedor = "",
    descricao = "",
    preco = "",
    quantEstoque = ""
    
    def __init__(self, produtoid, fornecedorid, descproduto, precoproduto, estoqueQuant):
        try:
            
            self.idproduto = produtoid
            self.idfornecedor = fornecedorid
            self.descricao = descproduto
            self.preco = precoproduto
            self.quantEstoque = estoqueQuant
            
        except Exception as e:
            print(str(e))
            
    
    #setters and getters         
            
    def set_idproduto(self, produtoid):
            self.idproduto = produtoid 

    try:
        def get_idproduto(self):
            return self.idproduto
    except Exception as e:
        print(str(e))
        
        
    def set_idfornecedor(self, fornecedorid):
            self.idfornecedor = fornecedorid 

    try:
        def get_idfornecedor(self):
            return self.idfornecedor
    except Exception as e:
        print(str(e))
        
    
    def set_descricao(self, descproduto):
            self.descricao = descproduto 

    try:
        def get_descricao(self):
            return self.descricao
    except Exception as e:
        print(str(e))
        
        
    def set_preco(self, precoproduto):
            self.preco = precoproduto 

    try:
        def get_preco(self):
            return self.preco
    except Exception as e:
        print(str(e))
        
        
    def set_quantEstoque(self, estoqueQuant):
            self.quantEstoque = estoqueQuant 

    try:
        def get_quantEstoque(self):
            return self.quantEstoque
    except Exception as e:
        print(str(e))