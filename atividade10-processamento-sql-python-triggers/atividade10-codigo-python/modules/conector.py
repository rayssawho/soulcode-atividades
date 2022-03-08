import mysql.connector


class Interface:
    user = ""
    password = ""
    host = ""
    database = ""

    def __init__(self, user, password, host, database):
        """Construtor da classe interface

        Args:
            user (string): usuário que acessa o banco de dados.
            password (string): senha do usuário que acessa o banco de dados.
            host (string): O endereço local (host) do banco de dados.
            database (string): o nome do banco de dados.
        """
        try:
            self.user = user
            self.password = password
            self.host = host
            self.database = database
        except Exception as e:
            print("ERRO no construtor:", str(e))

    def conectar(self):
        """Função que conecta ao banco de dados.

        Returns:
            self.user(string)
            self.password(string)
            self.host(string)
            self.database(string)
        """
        try:
            con = mysql.connector.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                database=self.database,
            )
            cursor = con.cursor()
            return con, cursor
        except Exception as e:
            print("ERRO na função conectar:", str(e))

    def desconectar(self, con, cursor):
        """Função para desconectar do banco de dados.

        Args:

        """

        try:
            cursor.close()
            con.commit()
            con.close()
        except Exception as e:
            print("ERRO na função desconectar:", str(e))

    def inserir(self, venda, produto, quantidade):
        """Função para inserir dados na tabela itensvenda no banco de dados

        Args:
            venda (string): recebe o código da venda.
            produto (string): recebe o código do produto.
            quantidade (string): recebe a quantidade do produto que será incluso na venda.

        Returns:

        """
        try:
            con, cursor = self.conectar()
            valores = '({}, "{}", {});'.format(venda, produto, quantidade)
            query = (
                "INSERT INTO itensvenda(venda, produto, quantidade) VALUES " + valores
            )
            cursor.execute(query)
            # print(query)
            return cursor.fetchall()
        except Exception as e:
            print("ERRO na função inserir:", str(e))
        finally:
            self.desconectar(con, cursor)

    def selecionar(self, o_que, de_onde, argumentos):
        """Função para selecionar qualquer tabela no banco de dados

        Args:
            o_que (string): Recebe o que queremos selecionar da tabela.
            de_onde (string): Recebe o nome da tabela que desejamos selecionar.
            argumentos (string): Recebe os argumentos da query.

        Returns:

        """
        try:
            con, cursor = self.conectar()
            query = "SELECT " + o_que + " FROM " + de_onde + argumentos + ";"
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)

    def deletar(self, codvenda):
        """Função para deletar qualquer venda da tabela itensvenda do banco de dados.

        Args:
            codvenda (string): recebe o código da venda que o usuário deseja deletar.

        Returns:

        """
        try:
            con, cursor = self.conectar()
            query = "DELETE FROM itensvenda WHERE venda = " + codvenda + ";"
            cursor.execute(query)
            # print(query)
            return cursor.fetchall()
        except Exception as e:
            print("ERRO na função deletar na classe interface_db:", str(e))
        finally:
            self.desconectar(con, cursor)

    def update(self):
        """Trigger para atualizar a quantidade de determinado item em estoque quando o mesmo for adicionado a tabela itensvenda

        Returns:

        """
        try:
            con, cursor = self.conectar()
            query = "CREATE TRIGGER tgr_itensvenda_Insert AFTER INSERT ON itensvenda FOR EACH ROW BEGIN UPDATE produtos SET estoque = estoque - new.quantidade WHERE referencia = new.produto; END;"
            print(query)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print("ERRO na função trigger_update", str(e))
        finally:
            self.desconectar(con, cursor)

    def apagar(self):
        """Trigger para devolver a quantidade em estoque dos produtos que foram retirados da tabela itensvenda

        Returns:

        """
        try:
            con, cursor = self.conectar()
            query = "CREATE TRIGGER tgr_itensvenda_delete after delete on itensvenda for each row begin update produtos set estoque = estoque + old.quantidade where referencia = old.produto; END;"
            print(query)
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print("ERRO na função trigger_delete", str(e))
        finally:
            self.desconectar(con, cursor)
