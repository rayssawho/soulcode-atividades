from modules.trata_dados import Dados_SQL, Dados_NoSQL
from modules.consultas_gerenciais import Consultas_Gerenciais
import pandas as pd

    
if __name__ == "__main__":
    
    try:
        while True:
            
            # Menu que serve para direcionar as ações do programa
            escolha = input("\n[1] - Ler os dados do Sistema A e enviar para o MySQL \
                            \n[2] - Ler os dados do Sistema B e enviar para o Cassandra \
                            \n[3] - Ler os Dados do MySQL, tratar e enviar para o Cassandra \
                            \n[4] - Ler os Dados do Cassandra \
                            \n[5] - Consultas Gerenciais \
                            \n[X] - Sair \
                            \n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\
                            \nEscolha uma das opções: ").upper()
            
            if escolha == '1':
                
                # Mensagem que verifica a intenção do usuário de enviar os dados para o MySQL
                confirmacao = input("Tem certeza de que deseja enviar os dados para o MySQL? S/N ").upper()
                
                if confirmacao == 'S':
                    
                    # Leitura do arquivo csv e transformação em DataFrame com o método read_csv do módulo pandas
                    df_dados = pd.read_csv('Sistema_A_SQL.csv')
                    
                    # Método que envia os dados do DataFrame para o MySQL
                    Dados_SQL.envia_dados_sql(df_dados)
                    
                else:
                    break
                
            elif escolha == '2':
                
                # Mensagem que verifica a intenção do usuário de enviar os dados para o Cassandra
                confirmacao = input("Tem certeza de que deseja enviar os dados para o Cassandra? S/N ").upper()
                
                if confirmacao == 'S':
                    
                    # Leitura do arquivo csv e transformação em DataFrame com o método read_csv do módulo pandas
                    df_dados = pd.read_csv('Sistema_B_NoSQL.csv')
                    
                    # Método que envia os dados do DataFrame para o Cassandra
                    Dados_NoSQL.envia_dados_nosql(df_dados)
                    
                else:
                    break
                
            elif escolha == '3':
                
                # Método que consulta os dados do MySQL, os trata e os envia para o Cassandra, se o usuário assim quiser.                
                Dados_SQL.consulta_e_trata_dados_sql()
                
            elif escolha == '4':
                
                # Método que executa uma consulta resumida dos dados do Cassandra
                Dados_NoSQL.consulta_tabela_Cassandra()
                
            elif escolha == '5':
                
                # Método que executa consultas gerenciais ao banco de dados no Cassandra
                Consultas_Gerenciais.consultas()
                
            # Método que encerra o programa    
            elif escolha == 'X':
                break
            
            else:
                print("Opção inválida")
                
    except Exception as e:
        print(str(e))
        
    
        