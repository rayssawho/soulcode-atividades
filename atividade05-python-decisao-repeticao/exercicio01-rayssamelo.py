#1) Crie um código que apresenta "Parabéns!" caso o usuário insira em sequência os números 1, 2, 3, e 4

try:
    
    print("Vamos jogar?")
    print("---> Qual é a senha? <---")
    print("Victor usa senhas super seguras em seus aplicativos, porém sua memória não é das melhores!")
    print("Vamos ajudá-lo a recuperar sua senha?")
    print("Dica: O Victor sempre usa 4 dígitos e sequências númericas em suas senhas!")
    senhacorreta = int(input("Digite uma sequência de 4 dígitos: "))

except Exception as e:
    print(str(e))

try:
    
    while senhacorreta != 1234:
        print("Infelizmente você não acertou a senha do Victor.")
        print("Que tal tentar novamente?")
        senhacorreta = int(input("Digite uma sequência de 4 dígitos: "))
    else:
        print("Parabéns!")
        print("Você acertou a super senha do Victor!")
        print("Fim de Jogo!")
        

except Exception as e:
    print(str(e))
