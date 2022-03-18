from modules.pessoa import Pessoa
from modules.cliente import Cliente
from modules.funcionario import Funcionario
from modules.produto import Produto
from modules.venda import Venda
import pandas as pd



if __name__ == "__main__":

    print("---> Hi Store <---")
    print()
    print("Escolha a opção desejada:")
    print(" 1 - Cadastrar Cliente ""\n", "2 - Cadastrar Funcionário" "\n", "3 - Cadastrar Produto" "\n", 
          "4 - Adicionar nova venda""\n", "5 - Listar Clientes", "\n", "6 - Listar Funcionários", "\n", 
          "7 - Listar Produtos", "\n", "8 - Listar Vendas", "\n", "0 - Sair", "\n")
    
    escolha1 = str(input())
    
    lista_clientes = []
    lista_funcionarios = []
    lista_produtos = []
    lista_vendas = []
      
    try:
        
       
        while escolha1 != 0:
           
            if escolha1 == "1":
                try:
                    
                    cliente1 = Cliente(input(str("Digite o nome do Cliente: ")),
                                        input(str("Digite o número do documento: ")), 
                                        input(str("Digite o endereço do Cliente: ")), 
                                        input(str("Digite o Telefone: ")), 
                                        input(str("Digite um ID para o Cliente: ")), 
                                        int(input("Quantidade de compras: ")),
                                        input(str("Digite a data de cadastro: ")))
                    
                    newcliente = [cliente1.get_nome(), cliente1.get_numero_doc(),
                                  cliente1.get_endereco(), cliente1.get_telefone(),
                                  cliente1.get_id_cliente(), cliente1.get_hist_compras(),
                                  cliente1.get_data_cadastro()]
                    
                                     
                    lista_clientes.append(list(newcliente))
                    
                    print("Cliente cadastrado com sucesso!")
                    
                    df_lista_clientes = pd.DataFrame(lista_clientes, columns = ['NomeCliente', 'DocumentoCliente', 
                                                                                'Endereco', 'Telefone',
                                                                                'IdCliente', 'QuantCompras',
                                                                                'Datacadastro'])
                    print(df_lista_clientes)
                    
                    print()
                    print("Escolha a opção desejada:")
                    print(" 1 - Cadastrar Cliente ""\n", "2 - Cadastrar Funcionário" "\n", "3 - Cadastrar Produto" "\n", 
                        "4 - Adicionar nova venda""\n", "5 - Listar Clientes", "\n", "6 - Listar Funcionários", "\n", 
                        "7 - Listar Produtos", "\n", "8 - Listar Vendas", "\n","0 - Sair", "\n")
                
                    escolha1 = str(input())
                
                except Exception as error:
                    print("Erro ao cadastrar novo cliente")
                    print()
                
                
        
                
            if escolha1 == "2":
                try:
                    funcionario1 = Funcionario(input(str("Digite o nome do Funcionário: ")), 
                                               input(str("Digite o número do documento: ")), 
                                               input(str("Digite o endereço: ")),
                                               input(str("Digite o Telefone: ")),
                                               input(str("Digite um ID para o funcionário: ")), 
                                               int(input("Quantidade de vendas:" )))
                    
                    
                    newfuncionario = [funcionario1.get_nome(), funcionario1.get_numero_doc(),
                                      funcionario1.get_endereco(), funcionario1.get_telefone(),
                                      funcionario1.get_id_func(), funcionario1.get_valor_vendas()]
                    
                                       
                    lista_funcionarios.append(newfuncionario)
                    
                    df_lista_funcionarios = pd.DataFrame(lista_funcionarios, columns = ['NomeFunc', 'DocumentoFunc', 'Endereco',
                                                                                        'Telefone', 'IdFunc',
                                                                                        'QuantVenda'])
                    print(df_lista_funcionarios)
                
                    print("Funcionário cadastrado com sucesso!")
                
                except Exception as error:
                    print("Erro ao cadastrar novo funcionário")
                
                print()
                print("Escolha a opção desejada:")
                print(" 1 - Cadastrar Cliente ""\n", "2 - Cadastrar Funcionário" "\n", "3 - Cadastrar Produto" "\n", 
                    "4 - Adicionar nova venda""\n", "5 - Listar Clientes", "\n", "6 - Listar Funcionários", "\n", 
                    "7 - Listar Produtos", "\n", "8 - Listar Vendas", "\n","0 - Sair", "\n")
                
                escolha1 = str(input())
                
            if escolha1 == "3":
                try:
                    produto1 = Produto(input(str("Digite o ID do produto: ")), 
                                       input(str("Digite o nome o produto: ")),
                                       input(str("Digite uma descrição do produto: ")), 
                                       int(input("Digite o valor unitário do produto:")), 
                                       int(input("Digite a quantidade em estoque: ")))
                    
                    newproduto = [produto1.get_id_produto(), produto1.get_nome_produto(), produto1.get_descricao(),
                                  produto1.get_valor(), produto1.get_estoque()]
                    
                                       
                    lista_produtos.append(newproduto)
                    
                    df_lista_produtos = pd.DataFrame(lista_produtos, columns = ['IdProduto', 'NomeProduto', 'Descricao',
                                                                                'ValorProduto', 'Estoque'])
                    
                    print(df_lista_produtos)
                
                    print("Produto Cadastrado com sucesso") 
                
                except Exception as error:
                    print("Erro ao cadastrar novo produto")
                
                print()
                print("Escolha a opção desejada:")
                print(" 1 - Cadastrar Cliente ""\n", "2 - Cadastrar Funcionário" "\n", "3 - Cadastrar Produto" "\n", 
                    "4 - Adicionar nova venda""\n", "5 - Listar Clientes", "\n", "6 - Listar Funcionários", "\n", 
                    "7 - Listar Produtos", "\n", "8 - Listar Vendas", "\n","0 - Sair", "\n")
                
                escolha1 = str(input())            
            
            if escolha1 == "4":
                try:
                    venda1 = Venda(str(input("Digite o ID da venda: ")), 
                                    str(input("Digite o ID do produto: ")),
                                    str(input("Digite o Id do cliente: ")),
                                    str(input("Digite o id do funcionário: ")),
                                    str(input("Valor total da venda: ")),
                                    int(input("Quantidade de Produtos: ")))
                    
                    newvenda = [venda1.get_id_venda(), venda1.get_produto_id(), venda1.get_cliente_id(),
                                venda1.get_func_id(), venda1.get_venda_valor(), venda1.get_quant_produto()]
                    
                    lista_vendas.append(newvenda)

                    df_lista_vendas = pd.DataFrame(lista_vendas, columns = ['IdVenda', 'IdProduto', 'IdCliente',
                                                                            'IdFunc', 'ValorTotal', 'QuantProduto'])
                    
                    print(df_lista_vendas)
                    
                except Exception as error:
                    print("Erro ao cadastrar nova venda")
                    
                try:
                    
                    for i in range(len(lista_produtos)):
                        if(lista_produtos[i][0] == lista_vendas[i][1]) and (lista_produtos[i][4]>= lista_vendas[i][5]):
                            lista_produtos[i][4] = lista_produtos[i][4] - lista_vendas[i][5]
                
                except Exception as error:
                    print("Erro ao atualizar o estoque")
                    
                try:
                    
                    for i in range(len(lista_clientes)):
                        if(lista_clientes[i][4] == lista_vendas[i][2]):
                            lista_clientes[i][5] = lista_vendas[i][5]
                
                except Exception as error:
                    print("Erro ao atualizar quantidade de compras do cliente")
                    
                try:
                
                    for i in range(len(lista_funcionarios)):
                        if(lista_funcionarios[i][4] == lista_vendas[i][3]):
                            lista_funcionarios[i][5] = lista_vendas[i][5]
                
                except Exception as error:
                    print("Erro ao atualizar quantidade de produtos vendidos do funcionário")            
                    
                print()                                  
                print("Escolha a opção desejada:")
                print(" 1 - Cadastrar Cliente ""\n", "2 - Cadastrar Funcionário" "\n", "3 - Cadastrar Produto" "\n", 
                    "4 - Adicionar nova venda""\n", "5 - Listar Clientes", "\n", "6 - Listar Funcionários", "\n", 
                    "7 - Listar Produtos", "\n", "8 - Listar Vendas", "\n","0 - Sair", "\n")
                                
                escolha1 = str(input())
                
            if escolha1 == "5":
                try:
                    print(lista_clientes)
                except Exception as error:
                    print("Erro ao listar clientes")
                
                print()    
                print("Escolha a opção desejada:")
                print(" 1 - Cadastrar Cliente ""\n", "2 - Cadastrar Funcionário" "\n", "3 - Cadastrar Produto" "\n", 
                    "4 - Adicionar nova venda""\n", "5 - Listar Clientes", "\n", "6 - Listar Funcionários", "\n", 
                    "7 - Listar Produtos", "\n", "8 - Listar Vendas", "\n","0 - Sair", "\n")
                
                escolha1 = str(input())  
            
            if escolha1 == "6":
                try:
                    print(lista_funcionarios)
                except Exception as error:
                    print("Erro ao listar funcionários")
                
                print()    
                print("Escolha a opção desejada:")
                print(" 1 - Cadastrar Cliente ""\n", "2 - Cadastrar Funcionário" "\n", "3 - Cadastrar Produto" "\n", 
                    "4 - Adicionar nova venda""\n", "5 - Listar Clientes", "\n", "6 - Listar Funcionários", "\n", 
                    "7 - Listar Produtos", "\n", "8 - Listar Vendas", "\n","0 - Sair", "\n")
                
                escolha1 = str(input())  
            
            if escolha1 == "7":
                try:
                    print(lista_produtos)
                except Exception as error:
                    print("Erro ao listar produtos")
                
                print()    
                print("Escolha a opção desejada:")
                print(" 1 - Cadastrar Cliente ""\n", "2 - Cadastrar Funcionário" "\n", "3 - Cadastrar Produto" "\n", 
                    "4 - Adicionar nova venda""\n", "5 - Listar Clientes", "\n", "6 - Listar Funcionários", "\n", 
                    "7 - Listar Produtos", "\n", "8 - Listar Vendas", "\n","0 - Sair", "\n")
                
                escolha1 = str(input())  
            
            if escolha1 == "8":
                try:
                    print(lista_vendas)
                except Exception as error:
                    print("Erro ao listar vendas")
                
                print()
                print("Escolha a opção desejada:")
                print(" 1 - Cadastrar Cliente ""\n", "2 - Cadastrar Funcionário" "\n", "3 - Cadastrar Produto" "\n", 
                    "4 - Adicionar nova venda""\n", "5 - Listar Clientes", "\n", "6 - Listar Funcionários", "\n", 
                    "7 - Listar Produtos", "\n", "8 - Listar Vendas", "\n","0 - Sair", "\n")
                
                escolha1 = str(input())  
            
            if escolha1 == "0":
                break
                
    except Exception as e:
        print(str(e))
    
        