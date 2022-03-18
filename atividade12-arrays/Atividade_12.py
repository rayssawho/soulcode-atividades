# arr = np.array([[1, 1, 150], [1, 2, 200], [1, 3, 78], [1, 2,50], [2, 1, 150], [2, 2, 200], [2, 3, 78], [2, 2,50]])
# desenvolva um código em Python que, considerando os dados como [id do vendedor, id do cliente, total da vena] calcule e apresente:
# - qual o id do vendedor que fez o maior valor total em vendas
# - qual o cliente que fez o maior numero de compras

#Grupo: Aldeise Barbosa, Rayssa Alcântara, Wesley Aranha

import numpy as np

arr = np.array([[1, 1, 150], [1, 2, 200], [1, 3, 78], [1, 2,50], [2, 1, 150], [2, 2, 200], [2, 3, 78], [2, 2,50]])
total_vendendores = [0, 0]
total_clientes = [0, 0, 0]

while True:
    try:
        selecao = int(input("[1] para receber relação vendedor\n [2] para relação cliente:\n [0] SAIR: "))
        try:
            if selecao == 1:
                for i in range(len(arr)):
                    if arr[i][0] == 1:
                        total_vendendores[0] += arr[i][2]
                    elif arr[i][0] == 2:
                        total_vendendores[1] += arr[i][2]
                print("Total vendedores: ", total_vendendores)
        except Exception as e:
            print(str(e))
        
        try:
            if selecao == 2:
                for i in range(len(arr)):
                    if arr[i][1] == 1:
                        total_clientes[0] = total_clientes[0] + arr[i][2]
                    elif arr[i][1] == 2:
                        total_clientes[1] += arr[i][2] 
                    elif arr[i][1] == 3:
                        total_clientes[2] += arr[i][2]
                print("Total clientes: ", total_clientes)
        except Exception as e:
            print(str(e))
        
        
        try:            
            if selecao == 0:
                break
        except Exception as e:
            print(str(e))
    
    except Exception as e:
        print(str(e))