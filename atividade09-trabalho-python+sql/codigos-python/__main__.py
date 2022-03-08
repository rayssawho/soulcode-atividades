from modules.connector import interface
from classes.fornecedor import fornecedor
from classes.produto import produto
from classes.vendas import vendas
from classes.vendedor import vendedor



if __name__ == "__main__":
    
    try:
        #conectando ao banco de dados:
        
        interface_bd = interface("user", "admin","127.0.0.1", "DROGARIA_PARAIBANA")
        
        
        
        print("---> Drogaria Paraibana <---")
        print()
        print("Escolha uma opção:")
        print()
        print("1 - Inserir vendas")
        print("2 - Total de Vendas")
        print("3 - Visualizar maior venda e Funcionário")
        print("4 - Visualizar Funcionário com maior quantidade de vendas")
        print("5 - Visualizar fornecedor mais utilizado" )
        print("6 - Comissões dos vendedores")
        print("0 - para sair.")
        
        escolha = float(input())        

    except Exception as e:
        print(e)

    
    while escolha == 1:
        try:
            #inserindo dados na tabela vendas:
            
            valores = input("Digite a venda que você quer adicionar. Ex:(idproduto, idvendedor, valorTotal, comissao) *Use os ()")
            dadosInserir = interface_bd.inserir("vendas", "(idproduto, idvendedor, valorTotal, comissao)", valores)
            print()
            print("1 - Inserir vendas")
            print("2 - Total de Vendas")
            print("3 - Visualizar maior venda e Funcionário")
            print("4 - Visualizar Funcionário com maior quantidade de vendas")
            print("5 - Visualizar fornecedor mais utilizado" )
            print("6 - Comissões dos vendedores")
            print("0 - para sair.")
            
            escolha = float(input())
        
        except Exception as e:
            print(str(e))    
    
    while escolha == 2:
        try:
                #o total de vendas:
                
            totalVendas = interface_bd.selecionar("count(vendas.idvenda)", "vendas", "")
            print("O Total de vendas é: ", totalVendas)
            print()    
            print("1 - Inserir vendas")
            print("2 - Total de Vendas")
            print("3 - Visualizar maior venda e Funcionário")
            print("4 - Visualizar Funcionário com maior quantidade de vendas")
            print("5 - Visualizar fornecedor mais utilizado" )
            print("6 - Comissões dos vendedores")
            print("0 - para sair.")
            print()
            escolha = float(input())
        
        except Exception as e:
            print(str(e))

    while escolha == 3:
        try:
            #o funcionário que realizou a maior venda e qual o total desta:
            
            maiorVenda = interface_bd.selecionar("max(vendas.valorTotal), vendedor.nome", "vendas", " JOIN vendedor ON vendedor.idvendedor = vendas.idvendedor")
            print("A maior venda e o vendedor(a) que a realizou foi: ", maiorVenda)
            print()
            print("1 - Inserir vendas")
            print("2 - Total de Vendas")
            print("3 - Visualizar maior venda e Funcionário")
            print("4 - Visualizar Funcionário com maior quantidade de vendas")
            print("5 - Visualizar fornecedor mais utilizado" )
            print("6 - Comissões dos vendedores")
            print("0 - para sair.")
            print()
            escolha = float(input()) 
        
        except Exception as e:
            print(str(e))
            
    while escolha == 4:    
        try:
            #o funcionário que realizou a maior quantidade de vendas e quantas foram:
            
            maiorQuantVenda = interface_bd.selecionar("vendedor.nome, count(*)", "vendas", " JOIN vendedor ON vendedor.idvendedor = vendas.idvendedor WHERE vendas.idvenda > 0 GROUP BY vendedor.nome ORDER BY count(*) DESC")
            print("O(a) vendedor(a) que realizou a maior quantidade de vendas, e quantas vendas foram realizadas foi:  ", maiorQuantVenda[0])
            print()
            print("1 - Inserir vendas")
            print("2 - Total de Vendas")
            print("3 - Visualizar maior venda e Funcionário")
            print("4 - Visualizar Funcionário com maior quantidade de vendas")
            print("5 - Visualizar fornecedor mais utilizado" )
            print("6 - Comissões dos vendedores")
            print("0 - para sair.")
            print()
            escolha = float(input()) 
        
        except Exception as e:
            print(str(e))
            
    while escolha == 5:        
        try:
            #o fornecedor mais utilizado:
            
            fornecedorMais = interface_bd.selecionar("fornecedor.nome, count(*)", "vendas", " INNER JOIN produto ON produto.idproduto = vendas.idproduto INNER JOIN fornecedor ON fornecedor.idfornecedor = produto.idfornecedor WHERE vendas.idproduto > 0 GROUP BY fornecedor.nome ORDER BY count(*) DESC")
            print("O Fornecedor mais utilizado é: ",fornecedorMais[0])
            print()
            print("1 - Inserir vendas")
            print("2 - Total de Vendas")
            print("3 - Visualizar maior venda e Funcionário")
            print("4 - Visualizar Funcionário com maior quantidade de vendas")
            print("5 - Visualizar fornecedor mais utilizado" )
            print("6 - Comissões dos vendedores")
            print("0 - para sair.")
            print()
            escolha = float(input()) 

        except Exception as e:
            print(str(e))
            
    while escolha == 6:
        
        try:
            #o total de comissão devido a cada funcionário considerando-se 8% de comissão:
            
            totalComissao = interface_bd.selecionar("vendedor.nome, vendas.comissao", "vendas", " JOIN vendedor ON vendedor.idvendedor = vendas.idvendedor GROUP BY vendedor.nome ORDER BY vendas.comissao DESC")
            print(totalComissao)
            print()
            print("1 - Inserir vendas")
            print("2 - Total de Vendas")
            print("3 - Visualizar maior venda e Funcionário")
            print("4 - Visualizar Funcionário com maior quantidade de vendas")
            print("5 - Visualizar fornecedor mais utilizado" )
            print("6 - Comissões dos vendedores")
            print("0 - para sair.")
            print()
            escolha = float(input()) 
            
        except Exception as e:
            print(str(e))
            