from modules.connector_cassandra import Interface_Cassandra
from modules.connector_MySQL import Interface_MySQL
import pandas as pd

class Dados_SQL:
    
    def envia_dados_sql(df_dados):
        """Método que recebe os dados de um dataFrame e os envia para a tabela 'vendas' no banco 'oldtech' no MySQL, 
        por meio de uma conexão que utiliza métodos do módulo connector_MySQL
        """
        try:
            
            # Laço que extrai valores do DataFrame e atribui às variáveis que são utilizadas na formação da string que funcionará como query SQL
            for i in range(len(df_dados)):
                nota_fiscal = df_dados.iloc[i,0]
                vendedor = df_dados.iloc[i,1]
                total = df_dados.iloc[i,2]
                insert = f"INSERT INTO oldtech.`vendas`(nota_fiscal, vendedor, total) VALUES ({nota_fiscal},'{vendedor}',{total});"
                
                # Conexão com o banco MySQL
                interface_sql = Interface_MySQL()
                
                # Método que envia as queries individualmente para o banco MySQL
                interface_sql.inserir(insert)
                
            # Mensagem de confirmação da conclusão do envio dos dados para o MySQL. 
            print("Dados enviados para MySQL.OLDTech.Vendas")

        except Exception as e:
            print(str(e))
            
    def consulta_e_trata_dados_sql():
        """Método que faz a consulta dos dados contidos na tabela 'vendas' no MySQL,
        os transforma em DataFrame, via método do Pandas, 
        exclui o campo redundante, para que os dados possam ser enviados para o Cassandra,
        e envia os dados para o Cassandra, utilizando métodos do módulo connector_cassandra
        """
        try:
            while True:
                
                # Conexão com o MySQL e utilzação do método acessar, para ler os dados da tabela 'vendas'
                dados = Interface_MySQL().acessar()
                
                # Transformação dos dados lidos em DataFrame    
                df_dados = pd.DataFrame(dados)
                
                # Ajuste dos nomes das colunas para exibição ao usuário
                df_dados.rename(columns={0:'ID', 1:'Nota Fiscal',2:'Vendedor',3:'Total'}, inplace=True)
                
                # Exclusão da coluna redundante
                df_dados.pop('ID') 
                
                # Exibição do conteúdo do DataFrame
                print (df_dados)
                
                # Mensagem que verifica a intenção do usuário de enviar os dados para o Cassandra
                decisao = input("Deseja enviar estes dados para o Cassandra? S/N ").upper()
                
                if decisao == 'S':
                    
                    # Invocação do método que envia dados para o Cassandra
                    Dados_NoSQL.envia_dados_nosql(df_dados)
                    break
                
        except Exception as e:
            print(str(e))
        
            
class Dados_NoSQL:
    
    def envia_dados_nosql(df_dados):
        """Método que recebe os dados de um dataFrame,
        e os envia para a família 'vendas' na keyspace 'oldtech' no Cassandra,
        por meio de métodos do módulo connector_cassandra
        """
        
        try:            
            # Laço que faz a leitura dos dados do Dataframe e os distribui em variáveis que fazem parte da query a ser enviada ao Cassandra
            query = ""
            for i in range(len(df_dados)):
                nota_fiscal = df_dados.iloc[i,0]
                vendedor = df_dados.iloc[i,1]
                total = df_dados.iloc[i,2]
                string = f"INSERT INTO vendas (id_venda, nota_fiscal, vendedor, total) VALUES (uuid(), {nota_fiscal}, '{vendedor}', {total});"
                query = query + string
                
            # Método que faz a concatenação de todas as queries geradas
            query = "BEGIN BATCH " + query + "APPLY BATCH;"
            
            # Método que formata a query resultante para ser enviada ao Cassandra como 'Batch'
            con = Interface_Cassandra('oldtech')
            con.inserir(query)
            
            # Mensagem de confirmação da conclusão do envio dos dados para o Cassandra. 
            print("Dados enviados para Cassandra.OLDTech.Vendas")  

        except Exception as e:
            print(str(e))
            
    def consulta_tabela_Cassandra():
        """Método que executa uma consulta na família 'vendas' no banco de dados 'oldtech' no Cassandra,
        utilizando métodos do módulo connector_cassandra.
        """
        
        try:
            
            # Conexão com o banco de dados e transformação dos dados em DataFrame
            dados = Interface_Cassandra.buscar(Interface_Cassandra)
            df_dados = pd.DataFrame(dados)
            
            # Exclusão da coluna 'id_venda' para melhorar a visualização
            df_dados.pop('id_venda')
                
            print(df_dados)
            
        except Exception as e:
            print(str(e))