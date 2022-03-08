
class vendas:
    idvenda = "",
    idproduto = "",
    idvendedor = "",
    valorTotal = "",
    comissao = ""
    
    def __init__(self, vendaid, produtoid, vendedorid, total, comissaovend):
        try:
            
            self.idvenda = vendaid
            self.idproduto = produtoid
            self.idvendedor = vendedorid
            self.valorTotal = total
            self.comissao = comissaovend
            
        except Exception as e:
            print(str(e))
            
    
    #setters and getters         
            
    def set_idvenda(self, vendaid):
            self.idvenda = vendaid 

    try:
        def get_idvenda(self):
            return self.idvenda
    except Exception as e:
        print(str(e))
    
    def set_idproduto(self, produtoid):
            self.idproduto = produtoid

    try:
        def get_idproduto(self):
            return self.idproduto
    except Exception as e:
        print(str(e))
        
    def set_idvendedor(self, vendedorid):
            self.idvendedor = vendedorid

    try:
        def get_idvendedor(self):
            return self.idvendedor
    except Exception as e:
        print(str(e))    
    
    def set_valorTotal(self, total):
            self.valorTotal = total

    try:
        def get_valorTotal(self):
            return self.valorTotal
    except Exception as e:
        print(str(e))        
    
    def set_comissao(self, comissaovend):
            self.comissao = comissaovend

    try:
        def get_comissao(self):
            return self.comissao
    except Exception as e:
        print(str(e))        
    
    
    
           
    