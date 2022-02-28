from modules.connector_cassandra import Interface_Cassandra
import pandas as pd

class Consultas_Gerenciais:

    def consultas():
        """Método que executa consultas gerenciais sobre os dados de vendas no Cassandra
        """
        
        try: 
            
            while True:
                            
                consulta = input("\n[1] - Consultar vendas sem vendedores cadastrados\
                                    \n[2] - Consultar vendas por vendedor\
                                    \n[3] - Consultar vendas por NF\
                                    \n[4] - Consultar valor total de vendas\
                                    \n[5] - Consultar valor médio das vendas\
                                    \n[6] - Consultar maior e menor vendas\
                                    \n[7] - Consultar vendas por valor (abaixo de)\
                                    \n[8] - Consultar vendas por valor (entre)\
                                    \n[9] - Consultar vendas por valor (acima de)\
                                    \n[X] - Voltar ao menu principal \
                                    \n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\
                                    \nEscolha uma opção: ").upper()
                
                if consulta == '1':
                    
                    try:
                        dados = Interface_Cassandra.buscar(Interface_Cassandra," nota_fiscal, total "," vendas "," where vendedor = 'nan' allow filtering")
                        df_dados = pd.DataFrame(dados)
                        print(df_dados)
                        print()
                        print("Valor total de vendas sem vendedores cadastrados:", round(sum(df_dados['total']),2))
                        print("Quantidade de vendas sem vendedores cadastrados_:", df_dados['nota_fiscal'].count())

                    except Exception as e:
                        print(str(e))
                    
                elif consulta == '2':
                    
                    try:
                        
                        nome = input("Informe o nome do vendedor: ").title()
                        condicao = " where vendedor = '" + nome + "' allow filtering"
                        dados = Interface_Cassandra.buscar(Interface_Cassandra , " nota_fiscal, total "," vendas ", condicao)
                        df_dados = pd.DataFrame(dados)
                        print(df_dados)
                        print()
                        print(f"Valor total de vendas de {nome}: ", round(sum(df_dados['total']),2))
                        print(f"Quantidade de vendas de {nome}_:", df_dados['nota_fiscal'].count())

                    except Exception as e:
                        print(str(e))
                    
                elif consulta == '3':
                    
                    try:
                        
                        NF = input("Informe o nº da Nota Fiscal: ").title()
                        condicao = " where nota_fiscal = " + NF + " allow filtering"
                        dados = Interface_Cassandra.buscar(Interface_Cassandra , " id_venda, nota_fiscal, total "," vendas ", condicao)
                        df_dados = pd.DataFrame(dados)
                        print(df_dados)
                        print()                            
                        print(f"Quantidade de NF de nº{NF}:", df_dados['nota_fiscal'].count())
                        
                    except Exception as e:
                        print(str(e))
                    
                elif consulta == '4':
                    
                    try:
                        dados = Interface_Cassandra.buscar(Interface_Cassandra," nota_fiscal, total "," vendas ")
                        df_dados = pd.DataFrame(dados)
                        print()
                        print("Valor total de vendas :", round(sum(df_dados['total']),2))
                        print("Quantidade de vendas__:", df_dados['nota_fiscal'].count())

                    except Exception as e:
                        print(str(e))
                    
                elif consulta == '5':
                    
                    try:
                        dados = Interface_Cassandra.buscar(Interface_Cassandra," total "," vendas ")
                        df_dados = pd.DataFrame(dados)
                        print()
                        print("Valor médio das vendas:", round(df_dados['total'].mean(),2))

                    except Exception as e:
                        print(str(e))
                    
                elif consulta == '6':
                    
                    try:
                        dados = Interface_Cassandra.buscar(Interface_Cassandra,"total "," vendas ")
                        df_dados = pd.DataFrame(dados)
                        print()
                        print("Venda de menor valor:", round(df_dados['total'].min(),2))
                        print("Venda de maior valor:", round(df_dados['total'].max(),2))

                    except Exception as e:
                        print(str(e))
                    
                elif consulta == '7':
                    
                    try:
                        
                        valor = input("Consultar vendas com valor abaixo de: ")
                        condicao = " where total < " + valor + " allow filtering"
                        dados = Interface_Cassandra.buscar(Interface_Cassandra , " id_venda, nota_fiscal, total "," vendas ", condicao)
                        df_dados = pd.DataFrame(dados)
                        print(df_dados)
                        print()                            
                        print(f"Quantidade de vendas com valor abaixo de {valor}:", df_dados['nota_fiscal'].count())
                        
                    except Exception as e:
                        print(str(e))
                    
                elif consulta == '8':
                    
                    try:
                        
                        valor_menor = input("Consultar vendas com valor maior do que: ")
                        valor_maior = input("e menor do que_________________________: ")
                        condicao = " where total >= " + valor_menor + " and total <= " + valor_maior + " allow filtering"
                        dados = Interface_Cassandra.buscar(Interface_Cassandra , " id_venda, nota_fiscal, total "," vendas ", condicao)
                        df_dados = pd.DataFrame(dados)
                        print(df_dados)
                        print()                            
                        print(f"Quantidade de vendas com valor entre {valor_menor} e {valor_maior}:", df_dados['nota_fiscal'].count())
                        
                    except Exception as e:
                        print(str(e))
                
                elif consulta == '9':
                    
                    try:
                        
                        valor = input("Consultar vendas  com valor acima de: ")
                        condicao = " where total > " + valor + " allow filtering"
                        dados = Interface_Cassandra.buscar(Interface_Cassandra , " id_venda, nota_fiscal, total "," vendas ", condicao)
                        df_dados = pd.DataFrame(dados)
                        print(df_dados)
                        print()                            
                        print(f"Quantidade de vendas com valor acima de {valor}:", df_dados['nota_fiscal'].count())
                        
                    except Exception as e:
                        print(str(e))
                
                elif consulta == 'X':
                    
                    break
                
                else:
                    print("Opção inválida")
                    
        except Exception as e:
            print(str(e))