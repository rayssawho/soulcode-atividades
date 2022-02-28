#5) Crie um código que conte por quantos segundos uma tecla é pressionada.

from datetime import datetime

try:
       
    print("Tente ser Rápido!")
    print("Digite qualquer tecla em seu teclado, aperte enter, e digite a segunda tecla e aperte enter novamente.")
    print("Tente ser o mais rápido possível")
    print("Quando estiver pronto, pode começar.")
    print("Aperte espaço e enter para sair.")
        
    
    tecla = input()
    hora = datetime.now()
    while tecla != " ":
        print("Foi pressionada a tecla: ", tecla , "às ", hora)
    
        print("Agora pressione outra tecla: ")
        tecla2 = input()
        hora2 = datetime.now()
        print("Foi pressionada a tecla: ", tecla2 , "às ", hora2)
        if tecla2 != " ":
            tempototal = hora2 - hora

            print("Seu tempo foi de: ", tempototal)
            print("Você consegue fazer melhor?")
            print("Quando estiver pronto, pode começar.")
        
        tecla = input()
        hora = datetime.now()
        
    
except Exception as e:
    print(str(e))