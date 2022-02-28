import mysql.connector 


class Interface_MySQL:
    
    def __init__(self, usuario="root", senha="Faxte76!@H1*", host="127.0.0.1", banco="oldtech"):
        """Construtor da classe interface_db

        Args:
            usuario (string): usuario para conexao ao banco
            senha (string): senha para acesso ao banco
            host (string): string contendo o endereco do host
            banco (string): string contendo o nome do banco
        """
        try:
            self.usuario = usuario
            self.senha = senha
            self.host = host
            self.banco = banco
        except Exception as e:
            print(str(e))
            
    
    def conectar(self):
        """Função que executa a conexão com o Banco de Dados

        """
        try:
            con = mysql.connector.connect(user=self.usuario, password=self.senha, host=self.host, database=self.banco)
            cursor = con.cursor()
            return con, cursor
        except Exception as e:
            print(str(e))
            
    def desconectar(self, con, cursor):
        """Função que faz o programa se desconectar do Banco de Dados

        Args:
            con (CMySQLConnection): Representa uma conexão aberta com o MySQL
            cursor (CMySQLCursor): Abre um cursor no MySQL
        """
        try:
            cursor.close()
            con.commit()
            con.close()
        except Exception as e:
            print(str(e))
               
    def acessar(self, o_que="*", de_onde="vendas"):
        """Executa Queries SQL

        Args:
            parametros (string): String com todos os parâmetros necessários para realizar uma Query SQL

        Returns:
            [cursor.fetchall()]: Mostra uma busca executada em todas as linhas da tabela pesquisada
        """
        
        try:
            con, cursor = self.conectar()
            query = f"SELECT {o_que} FROM {de_onde};"
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)
                       
            
    def inserir(self, query):
        """Executa Queries SQL

        Args:
            parametros (string): String com todos os parâmetros necessários para realizar uma Query SQL

        Returns:
            [cursor.fetchall()]: Mostra uma busca executada em todas as linhas da tabela pesquisada
        """
        
        try:
            con, cursor = self.conectar()
            cursor.execute(query)
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)