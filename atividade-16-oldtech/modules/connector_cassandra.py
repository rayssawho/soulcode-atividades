from cassandra.cluster import Cluster
cluster = Cluster()


class Interface_Cassandra:
    
    database="oldtech"

    def __init__(self, database):
        """Construtor da classe Interface_Cassandra

        Args:
            database (string): Nome do banco de dados(Keyspace)
        """
        self.database = database        
        

    def buscar(self, colunas = '*', tabela = 'vendas', where=""):
        """Método de busca de dados na tabela(família) 'vendas' no Cassandra

        Args:
            tabela (str, optional): Pode ser alterado, mas por padrão tem o valor 'vendas'
            colunas (str, optional): Pode ser alterado, mas por padrão tem o valor '*'

        Returns:
            [type]: Retorna os dados da pesquisa feita ao banco de DadosCassandra
        """
        try:
            session = cluster.connect("oldtech")
            query = f"SELECT {colunas} FROM {tabela}{where};"
            return session.execute(query)  
        except Exception as e:
            print(str(e))
            
    def inserir(self, query):
        """[summary]

        Args:
            query ([type]): [description]
        """
        try:
            session = cluster.connect(self.database)
            session.execute(query)
        except Exception as e:
            print(str(e))