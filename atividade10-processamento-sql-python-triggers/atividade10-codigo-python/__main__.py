# Atividade 10 - Processamento SQL e Python
# @Aldeise Barbosa --- @Aurélia ---
# @Daniel Viccari --- @Leila Roque ---
# @Pedro Heeger --- @Rayssa Melo.

from modules.conector import Interface

if __name__ == "__main__":

    try:
        # chama a função que conecta ao banco de dados

        interface_banco = Interface("user", "admin", "127.0.0.1",
                                    "AULA_17_11_21")

        while True:
            # cria um "Menu" para facilitar
            # a execução das funções pelo usuário

            print(
                "1-Criar Trigger Update \n \
                    2-Criar Trigger Delete \n \
                        3-Inserir dados \n \
                            4-Deletar dados \n \
                                5-Selecionar tabela \n \
                                    0-Sair \n"
            )
            selecao = input("Digite uma opção: ")

            if selecao == "1":
                # chama o Trigger para atualizar a quantidade em estoque

                dados1 = interface_banco.update()

            elif selecao == "2":
                # chama o Trigger para devolver
                # a quantidade em estoque quando a venda é apagada
                dados2 = interface_banco.apagar()

            elif selecao == "3":
                # chama a função Inserir que
                # adiciona dados na tabela itensvenda
                venda = input("Digite o numero da venda: ")
                produto = input("Digite o código do produto: ")
                quantidade = input("Digite a quantidade: ")
                dados3 = interface_banco.inserir(venda, produto, quantidade)

            elif selecao == "4":
                # chama a função deletar para excluir
                # uma venda na tabela itensvenda
                codvenda = input("Digite o código da venda: ")
                delete = interface_banco.deletar(codvenda)

            elif selecao == "5":
                # chama a função selecionar para
                # visualizar qualquer tabela no banco de dados
                tabela = input("Digite o nome da tabela: ")
                print()
                select = interface_banco.selecionar("*", tabela, "")
                for row in select:
                    print(str(row))
                print()

            elif selecao == "0":
                # finaliza o programa
                break

    except Exception as e:
        print("ERRO no main:", str(e))
