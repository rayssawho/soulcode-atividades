#4) Crie um código que receba 2 números e resolva a potencia do primeiro ao segundo. Ex: 5², 3³, ...

try:

    print("Vamos Calcular potencias!")
    print("A potencia será do primeiro ao segundo valor que você digitar.")
    numero1 = float(input("Digite o primeiro valor: "))
    numero2 = float(input("Digite o segundo valor: "))


    while numero1 != 0:
        print("Você digitou ", numero1 ," e o resultado da potência com o número ", numero2 , " é:")
        print(numero1 ** numero2)
        numero1 = float(input("Digite o primeiro valor: "))
        numero2 = float(input("Digite o segundo valor: "))

except Exception as e:
    print(str(e))
