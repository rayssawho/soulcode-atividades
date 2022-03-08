import mysql.connector

class interface:
    usuario = "",
    senha = "",
    host = "",
    banco = ""
    
    def __init__(self, usuario, senha, host, banco):
        """[declaração de paramentos da classe interface]

        Args:
            usuario (string): usuário do banco de dados.
            senha (string): senha de acesso ao banco de dados.
            host (string): endereço host.
            banco (string): nome do banco de dados.
        """
        try:
           
            self.usuario = usuario
            self.senha = senha
            self.host = host
            self.banco = banco
         
        except Exception as e:
            print(str(e))
            
    def conectar(self):
        try:
            
            con = mysql.connector.connect(user = self.usuario, password = self.senha, host = self.host, database = self.banco)
            cursor = con.cursor()
            return con, cursor
            
        except Exception as e:
            print(str(e))
    
    def desconectar(self, con, cursor):
        try:
            cursor.close()
            con.commit()
            con.close()
        except Exception as e:
            print(str(e)) 
    
    def selecionar(self, o_que, de_onde, argumentos):
        try:
            con, cursor = self.conectar()
            query = "SELECT " + o_que + " FROM " + de_onde + argumentos + ";"
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)
            
    def inserir(self, nometabela, atributostabela, valores):
        try:
            con, cursor = self.conectar()
            query = "INSERT INTO " + nometabela + atributostabela + "VALUES " + valores + ";"
            print(query)
            cursor.execute(query)
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)
    
    
    