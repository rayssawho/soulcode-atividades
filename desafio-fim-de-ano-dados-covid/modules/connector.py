#CONECTOR POSTGRES
#==============================================

import psycopg2

class Interface_postgre:

    user, password, host, database = "", "", "", ""

    def __init__(self, user, password, host, database):
        """Construtor da classe Interface_db

        Args:
            usuario (string): recebe o nome do usuário para conectar com o banco de dados
            senha (string): recebe a senha do usuário para acessar o banco de dados
            host (string): recebe "localhost" ou o seu número
            banco (string): recebe nome do banco de dados
        """

        try:
            self.user = user
            self.password = password
            self.host = host
            self.database = database
        except Exception as e:
            print("Erro no construtor da classe Interface_postgre: ", str(e))
    


    def connect_postgre(self):
        try:
            connection = psycopg2.connect(user=self.user,
                                password=self.password,
                                host=self.host,
                                database=self.database)
            
            cursor = connection.cursor()
            return connection, cursor
        except Exception as e:
            print("Erro no método connect_postgre da classe interface_postgre: ", str(e))

    
    def desconnect_postgre(self, connection, cursor):
        try:
            cursor.close()
            connection.commit()
            connection.close()
        except Exception as e:
            print("Erro no método desconnect da classe interface_postgre: ", str(e))

    
    def selection_postgre(self, what, name_table, argument):
        try:
            connection, cursor = self.connect_postgre()
            selection_query = f"SELECT {what} FROM {name_table} {argument};"
            cursor.execute(selection_query)
            # for row in cursor:
            #     print(row)
            return cursor.fetchall()
        except Exception as e:
            print("Erro no método insert_db da classe interface_postgre: ", str(e))
        finally:
            self.desconnect_postgre(connection, cursor)



    def insert_postgre(self, where, column, insert_value):
        try:

            connection, cursor = self.connect_postgre()
            insert_query = f"INSERT INTO {where} ({column}) VALUES {insert_value};"
            cursor.execute(insert_query)
            print(insert_query)
        except Exception as e:
            print("Erro no método insert_db da classe interface_postgre: ", str(e))
        finally:
            self.desconnect_postgre(connection, cursor)

#=====================================================================
#CONECTOR CASSANDRA

from cassandra.cluster import Cluster


class Interface_cassandra:

    def connect_cassandra(self):
        try:
            cluster = Cluster()
            session = cluster.connect('covid_cases')
            return session
        except Exception as e:
            print("Erro ao se conectar no cassandra: ", str(e))


    
    def selection_cassandra(self, what, name_table, argument):
        try:
            # Conecta ao cassandra
            session = self.connect_cassandra()

            # Seleciona dados do banco de dados
            selection_query = f"SELECT {what} FROM {name_table} {argument};"
            data_cassandra = session.execute(selection_query)
            return data_cassandra.fetchall()
        except Exception as e:
            print("Erro no método insert_db da classe interface_Cassandra: ", str(e))



    def insert_cassandra(self, table_name, columns_names, insert_value):
        try:
            # Conecta ao cassandra
            session = self.connect_cassandra()

            # Query para inserir no cassandra
            query = f"INSERT INTO {table_name} ({columns_names}) VALUES {insert_value};"
            session.execute(query)
            print(query)
        except Exception as e:
            print("Erro ao inserir dados no cassandra: ", str(e))