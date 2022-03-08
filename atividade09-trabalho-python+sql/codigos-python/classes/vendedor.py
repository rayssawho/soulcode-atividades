
class vendedor:
    idvendedor = "",
    nome = "",
    cpf = "",
    endereco = "",
    telefone = ""
    
    def __init__(self, vendedorid, nomevendedor, cpfvendedor, endvendedor, telvendedor):
        try:
            
            self.idvendedor = vendedorid
            self.nome = nomevendedor
            self.cpf = cpfvendedor
            self.endereco = endvendedor
            self.telefone = telvendedor
            
        except Exception as e:
            print(str(e))
            
            
    #setters and getters         
            
    def set_idvendedor(self, vendedorid):
            self.idvendedor = vendedorid 

    try:
        def get_idvendedor(self):
            return self.idvendedor
    except Exception as e:
        print(str(e))
        
        
    def set_nome(self, nomevendedor):
            self.nome = nomevendedor 

    try:
        def get_nome(self):
            return self.nome
    except Exception as e:
        print(str(e))
        
    
    def set_cpf(self, cpfvendedor):
            self.cpf = cpfvendedor 

    try:
        def get_cpf(self):
            return self.cpf
    except Exception as e:
        print(str(e))
        
    
    def set_endereco(self, endvendedor):
            self.endereco = endvendedor 

    try:
        def get_endereco(self):
            return self.endereco
    except Exception as e:
        print(str(e))
        
        
    def set_telefone(self, telvendedor):
            self.telefone = telvendedor 

    try:
        def get_telefone(self):
            return self.telefone
    except Exception as e:
        print(str(e))