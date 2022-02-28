#6) Crie um código que receba em sequencia de produtos contendo nome de produto, descrição, preço e quantidade em estoque.



print("Cadastro de Mercadorias")
escolha = input("Aperte enter para começar:")

produtos = []
descricoes = []
precos = []
quantidades = []

tabela = produtos, descricoes, precos, quantidades 

try:
    while escolha != " ":     
        produto = str(input("Qual produto você deseja cadastrar?"))
        produtos.append(produto)
        for a in produtos:
            print(a)
            continue
        descricao = str(input("Digite uma breve descrição do Produto: "))
        descricoes.append(descricao)
        for a in descricoes:
            print(a)
            continue
        preco = float(input("Digite o preço do Produto: "))
        precos.append(preco)
        for a in precos:
            print(a)
            continue
        quantidade = float(input("Digite a quantidade do Produto em estoque: "))
        quantidades.append(quantidade)
        for a in quantidades:
            print(a)
            continue
        for a in tabela:
            print(a)
        
        print()
        print("Para sair digite espaço e enter")
        escolha = input("Para adicionar outro Produto, digite enter:")
        
        
        if escolha == " ":
            break
except Exception as e:
    print(str(e))