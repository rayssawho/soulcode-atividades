from classes import Series

if __name__ == "__main__":

    print("---> Hi Seriados <---")
    print()
    escolha = input(
                        str(
                            "1 - Cadastrar nova série"
                            "\n"
                            "2 - Listar séries Cadastradas"
                            "\n"
                        )
                    )

    cadastros_serie = []
    # for serie in cadastros_serie:
    #         print(serie)
    while escolha != 0:

        if escolha == "1":

            try:

                serie1 = Series(
                    input(str("Digite o nome da Série: ")),
                    input(str("Digite o genero da Série: ")),
                    input(str("Digite o nome do diretor:")),
                    input(str("Quem escreveu a série:")),
                    input(str("Qual canal ou streaming que a série está disponível: ")),
                    input(str("Qual o ano de lançamento: ")),
                    input(str("Quantas temporadas já foram lançadas: ")),
                )

                newserie = [
                    "Seriado: " + serie1.get_nome(),
                    "Genero: " + serie1.get_genero(),
                    "Direção: " + serie1.get_direcao(),
                    "Roteiro: " + serie1.get_roteiro(),
                    "Canal ou Streaming: " + serie1.get_canal(),
                    "Ano de Lançamento: " + serie1.get_ano_lancamento(),
                    "Temporadas Disponíveis: " + serie1.get_quant_temp(),
                ]

                cadastros_serie.append(newserie)

                escolha = input(
                    str(
                        "1 - Cadastrar nova série"
                        "\n"
                        "2 - Listar séries Cadastradas"
                        "\n"
                    )
                )

            except Exception as Error:
                print("Erro. Não foi possível cadastrar uma nova série")

        if escolha == "2":

            try:
                if cadastros_serie == []:
                    print("Nenhuma série cadastrada")
                    escolha = input(
                        str(
                            "1 - Cadastrar nova série"
                            "\n"
                            "2 - Listar séries Cadastradas"
                            "\n"
                        )
                    )
                else:
                    print(cadastros_serie)
                    escolha = input(
                        str(
                            "1 - Cadastrar nova série"
                            "\n"
                            "2 - Listar séries Cadastradas"
                            "\n"
                        )
                    )
            except Exception as Error:
                print("Erro ao listar as séries cadastradas")
