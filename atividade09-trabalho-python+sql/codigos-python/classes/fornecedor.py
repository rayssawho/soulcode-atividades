
class fornecedor:
    idfornecedor = "",
    nome = "",
    cnpj = ""
    
    def __init__(self, fornecedorid, nomefornec, cnpjfornec):
        try:
            
            self.idfornecedor = fornecedorid
            self.nome = nomefornec
            self.cnpj = cnpjfornec
            
        except Exception as e:
            print(str(e))
            
    
    #setters and getters         
            
    def set_idfornecedor(self, fornecedorid):
            self.idfornecedor = fornecedorid 

    try:
        def get_idfornecedor(self):
            return self.idfornecedor
    except Exception as e:
        print(str(e))
        
        
    def set_nome(self, nomefornec):
            self.nome = nomefornec 

    try:
        def get_nome(self):
            return self.nome
    except Exception as e:
        print(str(e))
        
        
    def set_cnpj(self, cnpjfornec):
            self.cnpj = cnpjfornec 

    try:
        def get_cnpj(self):
            return self.cnpj
    except Exception as e:
        print(str(e))
        
        