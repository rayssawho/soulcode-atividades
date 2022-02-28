#2) Crie um código que pede nomes em sequencia, e apresenta a lista completa conforme o usuário digita.


print("---> Escolha os Desafios <---")
print("1 - Escreva nomes dos personagens de Harry Potter, o máximo que conseguir.")
print("2 - Escreva nomes de marcas de veículos, o máximo que conseguir.")
print("3 - Escreva nomes de escritores do séc.XIX, o máximo que conseguir.")
print("0 - Sair!")

escolha = int(input("Digite o número da opção desejada: "))

personagens = []
marcas = []
escritores = []

try:
    while escolha == 1:
    
        personagem = str(input("Digite o nome do Personagem: "))
        if personagem == "0":
            break
        personagens.append(personagem) 
    for a in personagens: 
        print(a)

except Exception as e:
    print(e)          

try:
    while escolha == 2:
    
        marca = str(input("Digite o nome da marca de veículo: "))
        if marca == "0":
            break
        marcas.append(marca)
    for a in marcas:
        print(a)

except Exception as e:
    print(e)        

try:
    while escolha == 3:
    
        escritor = str(input("Digite o nome do escritor(a): "))
        if escritor == "0":
            break
        escritores.append(escritor)
    for a in escritores:
        print(a)

except Exception as e:
    print(e) 

try:           
    while escolha == 0:
        break

except Exception as e:
    print(e)  
    
else:
    print("1 - Escreva nomes dos personagens de Harry Potter, o máximo que conseguir.")
    print("2 - Escreva nomes de marcas de veículos, o máximo que conseguir.")
    print("3 - Escreva nomes de escritores do séc.XIX, o máximo que conseguir.")
    print("0 - Sair!")
    escolha = int(input("Digite o número da opção desejada: "))

  