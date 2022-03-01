from modules.connector import Interface_postgre
from modules.connector import Interface_cassandra
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max, min, col, regexp_replace, sum, count, when, isnull
from pyspark.sql import functions as B
from pyspark.sql.types import FloatType

"""Licença
Todas as visualizações, dados e códigos produzidos por Our World in Data têm acesso totalmente aberto sob a licença Creative Commons BY .
Permissão para usar, distribuir e reproduzi-los em qualquer meio.
Dados de vacinação:
Mathieu, E., Ritchie, H., Ortiz-Ospina, E. et al. Um banco de dados global de vacinações COVID-19. Nat Hum Behav (2021). https://doi.org/10.1038/s41562-021-01122-8
Dados de teste:
Hasell, J., Mathieu, E., Beltekian, D. et al. Um banco de dados cross-country de testes COVID-19. Sci Data 7 , 345 (2020). https://doi.org/10.1038/s41597-020-00688-8
Autores:
Dados foram coletados, agregados e documentados por Cameron Appel, Diana Beltekian, Daniel Gavrilov, Charlie Giattino, Joe Hasell, Bobbie Macdonald, Edouard Mathieu, Esteban Ortiz-Ospina, Hannah Ritchie, Lucas Rodés-Guirao, Max Roser.
"""


spark = SparkSession.builder.appName("OTR").config("spark.sql.caseSensitive", "True").getOrCreate()

if __name__ == '__main__':
    try:
        while True:
            print("\n")
            print("=========================================================================================")
            print("                    SEJA BEM-VINDO(A)!")
            print("=========================================================================================")
            print("""
                    MENU DE OPÇÕES

                    0-Sair do Menu
                    1-Inserir dados no SQL
                    2-Mudar os nomes das colunas e gerar o arquivo Parquet
                    3-Quantidade de dados processados
                    4-Óbitos na China no primeiro dia em que foi decretada a pandemia
                    5-Casos no Brasil no primeiro dia em que foi decretada a pandemia
                    """)
            
            print("========================================================================================")
            option = input("Selecione uma das opções: ")
            print("\n")


            if option == "0":
                print("========================================================")
                print("               PROGRAMA FINALIZADO!")
                print("========================================================")
                break


                            
                       
            
            if option == "1":
                try:
                    # Instanceando as classes:
                    Interface_db_postgre = Interface_postgre('postgres', 'admin', '127.0.0.1', 'covid_cases')
                    
                    
                    # Lendo o arquivo csv:
                    df_covid = pd.read_csv('./dados/owid-covid-data.csv')

                    # # Substitui dados vazios de todas as colunas  por 0.0 ou Null:
                    df_covid.update(df_covid['iso_code'].fillna("Null", inplace=True))
                    df_covid.update(df_covid['continent'].fillna("Null", inplace=True))
                    df_covid.update(df_covid['location'].fillna("Null", inplace=True))
                    df_covid.update(df_covid['date'].fillna("Null", inplace=True))
                    df_covid.update(df_covid['total_cases'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_cases'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_cases_smoothed'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['total_deaths'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_deaths'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_deaths_smoothed'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['total_cases_per_million'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_cases_per_million'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_cases_smoothed_per_million'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['total_deaths_per_million'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_deaths_per_million'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_deaths_smoothed_per_million'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['reproduction_rate'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['icu_patients'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['icu_patients_per_million'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['hosp_patients'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['hosp_patients_per_million'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['weekly_icu_admissions'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['weekly_icu_admissions_per_million'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['weekly_hosp_admissions'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['weekly_hosp_admissions_per_million'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_tests'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['total_tests'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['total_tests_per_thousand'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_tests_per_thousand'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_tests_smoothed'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_tests_smoothed_per_thousand'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['positive_rate'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['tests_per_case'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['tests_units'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['total_vaccinations'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['people_vaccinated'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['people_fully_vaccinated'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['total_boosters'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_vaccinations'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_vaccinations_smoothed'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['total_vaccinations_per_hundred'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['people_vaccinated_per_hundred'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['people_fully_vaccinated_per_hundred'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['total_boosters_per_hundred'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_vaccinations_smoothed_per_million'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_people_vaccinated_smoothed'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_people_vaccinated_smoothed_per_hundred'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['stringency_index'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['population'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['population_density'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['median_age'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['aged_65_older'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['aged_70_older'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['gdp_per_capita'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['extreme_poverty'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['cardiovasc_death_rate'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['diabetes_prevalence'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['female_smokers'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['male_smokers'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['handwashing_facilities'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['hospital_beds_per_thousand'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['life_expectancy'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['human_development_index'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['excess_mortality_cumulative_absolute'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['excess_mortality_cumulative'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['excess_mortality'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['excess_mortality_cumulative_per_million'].fillna(0.0, inplace=True))

                                                           
                    # Inseri dados no SQL :
                    columns_names = "iso_code, continent, location, date, total_cases, new_cases, new_cases_smoothed, total_deaths, new_deaths, new_deaths_smoothed, total_cases_per_million, new_cases_per_million, new_cases_smoothed_per_million, total_deaths_per_million, new_deaths_per_million, new_deaths_smoothed_per_million, reproduction_rate, icu_patients, icu_patients_per_million, hosp_patients, hosp_patients_per_million, weekly_icu_admissions, weekly_icu_admissions_per_million, weekly_hosp_admissions, weekly_hosp_admissions_per_million, new_tests, total_tests, total_tests_per_thousand, new_tests_per_thousand, new_tests_smoothed, new_tests_smoothed_per_thousand, positive_rate, tests_per_case, tests_units, total_vaccinations, people_vaccinated, people_fully_vaccinated, total_boosters, new_vaccinations,new_vaccinations_smoothed, total_vaccinations_per_hundred, people_vaccinated_per_hundred, people_fully_vaccinated_per_hundred, total_boosters_per_hundred, new_vaccinations_smoothed_per_million, new_people_vaccinated_smoothed, new_people_vaccinated_smoothed_per_hundred, stringency_index, population, population_density, median_age, aged_65_older, aged_70_older, gdp_per_capita, extreme_poverty, cardiovasc_death_rate, diabetes_prevalence, female_smokers, male_smokers, handwashing_facilities, hospital_beds_per_thousand, life_expectancy, human_development_index, excess_mortality_cumulative_absolute, excess_mortality_cumulative, excess_mortality, excess_mortality_cumulative_per_million"
                    table_name = "covid_data"
                    for i in range(len(df_covid)):
                        data_to_insert = df_covid.iloc[i, 0], df_covid.iloc[i, 1], df_covid.iloc[i, 2],df_covid.iloc[i, 3], df_covid.iloc[i, 4], df_covid.iloc[i, 5],df_covid.iloc[i, 6], df_covid.iloc[i, 7], df_covid.iloc[i, 8],df_covid.iloc[i, 9], df_covid.iloc[i, 10], df_covid.iloc[i, 11],df_covid.iloc[i, 12], df_covid.iloc[i, 13], df_covid.iloc[i, 14],df_covid.iloc[i, 15], df_covid.iloc[i, 16], df_covid.iloc[i, 17],df_covid.iloc[i, 18], df_covid.iloc[i, 19], df_covid.iloc[i, 20],df_covid.iloc[i, 21], df_covid.iloc[i, 22], df_covid.iloc[i, 23],df_covid.iloc[i, 24], df_covid.iloc[i, 25], df_covid.iloc[i, 26],df_covid.iloc[i, 27], df_covid.iloc[i, 28], df_covid.iloc[i, 29],df_covid.iloc[i, 30], df_covid.iloc[i, 31], df_covid.iloc[i, 32],df_covid.iloc[i, 33], df_covid.iloc[i, 34], df_covid.iloc[i, 35],df_covid.iloc[i, 36], df_covid.iloc[i, 37], df_covid.iloc[i, 38],df_covid.iloc[i, 39], df_covid.iloc[i, 40], df_covid.iloc[i, 41],df_covid.iloc[i, 42], df_covid.iloc[i, 43], df_covid.iloc[i, 44],df_covid.iloc[i, 45], df_covid.iloc[i, 46], df_covid.iloc[i, 47],df_covid.iloc[i, 48], df_covid.iloc[i, 49], df_covid.iloc[i, 50],df_covid.iloc[i, 51], df_covid.iloc[i, 52], df_covid.iloc[i, 53],df_covid.iloc[i, 54], df_covid.iloc[i, 55], df_covid.iloc[i, 56],df_covid.iloc[i, 57], df_covid.iloc[i, 58], df_covid.iloc[i, 59],df_covid.iloc[i, 60], df_covid.iloc[i, 61], df_covid.iloc[i, 62],df_covid.iloc[i, 63], df_covid.iloc[i, 64], df_covid.iloc[i, 65], df_covid.iloc[i, 66]
                        data_insert = Interface_db_postgre.insert_postgre(table_name, columns_names, data_to_insert)
                        
                    # Baixar o df gerado
                    df_covid.to_csv(r'D:\Curso BC8 Engenharia de Dados+Python\Visual Studio\caso_covid_novo.csv', index = False, header=True)
                    
                except Exception as e:
                    print("Erro ao enviar dados para o SQL: ", str(e))
                                      
            if option == "2":
                try:
                    # ------------------------------------------------------------------------------------------
                    # Importa e lê arquivo csv:
                    # ------------------------------------------------------------------------------------------
                    
                    dados_covid = spark.read.format("csv").option("header", "true")\
                            .option("delimiter", ";").option("InferSchema", "true")\
                            .option("encoding", "ISO-8859-1")\
                            .load(r'D:\Curso BC8 Engenharia de Dados+Python\Visual Studio\owid-covid-data.csv')

                   
                    # ------------------------------------------------------------------------------------------
                    # Renomeia colunas da tabela:
                    # ------------------------------------------------------------------------------------------
                    
                    dados_covid = dados_covid.select(dados_covid[0].alias("iso_code"),\
                        dados_covid[1].alias("continente"),\
                        dados_covid[2].alias("localizacao"),\
                        dados_covid[3].alias("data"),\
                        dados_covid[4].alias("total_de_casos"),\
                        dados_covid[5].alias("novos_casos"),\
                        dados_covid[6].alias("novos_casos_7_dias"),\
                        dados_covid[7].alias("total_de_mortes"),\
                        dados_covid[8].alias("novas_mortes"),\
                        dados_covid[9].alias("novas_mortes_suavizadas"),\
                        dados_covid[10].alias("total_de_casos_por_milhao"),\
                        dados_covid[11].alias("novos_casos_por_milhao"),\
                        dados_covid[12].alias("novos_casos_7_dias_por_milhao"),\
                        dados_covid[13].alias("total_de_mortes_por_milhao"),\
                        dados_covid[14].alias("novos_mortes_por_milhao"),\
                        dados_covid[15].alias("novas_mortes_suavizadas_por_milhao"),\
                        dados_covid[16].alias("taxa_de_reproducao"),\
                        dados_covid[17].alias("pacientes_em_UTI"),\
                        dados_covid[18].alias("pacientes_em_UTI_por_milhao"),\
                        dados_covid[19].alias("pacientes_em_hospitais"),\
                        dados_covid[20].alias("pacientes_em_hospitais_por_milhao"),\
                        dados_covid[21].alias("admissoes_em_UTI_semanais"),\
                        dados_covid[22].alias("admissoes_em_UTI_semanais_por_milhao"),\
                        dados_covid[23].alias("admissoes_em_hospitais_semanais"),\
                        dados_covid[24].alias("admissoes_em_hospitais_semanais_por_milhao"),\
                        dados_covid[25].alias("novo_testes"),\
                        dados_covid[26].alias("testes_totais"),\
                        dados_covid[27].alias("testes_totais_por_mil"),\
                        dados_covid[28].alias("novos_testes_por_mil"),\
                        dados_covid[29].alias("novos_testes_7_dias"),\
                        dados_covid[30].alias("novos_testes_7_dias_por_mil"),\
                        dados_covid[31].alias("taxa_positiva"),\
                        dados_covid[32].alias("testes_por_caso"),\
                        dados_covid[33].alias("unidades_de_teste"),\
                        dados_covid[34].alias("vacinacoes_totais"),\
                        dados_covid[35].alias("pessoas_vacinadas"),\
                        dados_covid[36].alias("pessoas_totalmente_vacinadas"),\
                        dados_covid[37].alias("reforcos_totais"),\
                        dados_covid[38].alias("novas_vacinacoes"),\
                        dados_covid[39].alias("novas_vacinacoes_7_dias"),\
                        dados_covid[40].alias("vacinacoes_totais_por_cem"),\
                        dados_covid[41].alias("pessoas_vacinadas_por_cem"),\
                        dados_covid[42].alias("pessoas_totalmente_vacinadas_por_cem"),\
                        dados_covid[43].alias("reforcos_totais_por_cem"),\
                        dados_covid[44].alias("novas_vacinacoes_7_dias_por_milhao"),\
                        dados_covid[45].alias("novas_pessoas_vacinadas_7_dias"),\
                        dados_covid[46].alias("novas_pessoas_vacinadas_7_dias_por_cem"),\
                        dados_covid[47].alias("indice_de_rigor"),\
                        dados_covid[48].alias("populacao"),\
                        dados_covid[49].alias("densidade_populacional"),\
                        dados_covid[50].alias("idade_mediana"),\
                        dados_covid[51].alias("65_anos"),\
                        dados_covid[52].alias("70_anos"),\
                        dados_covid[53].alias("PIB_per_capita"),\
                        dados_covid[54].alias("pobreza_extrema"),\
                        dados_covid[55].alias("taxa_de_mortalidade_cardiovascular"),\
                        dados_covid[56].alias("prevalencia_de_diabetes"),\
                        dados_covid[57].alias("mulheres_fumantes"),\
                        dados_covid[58].alias("homens_fumantes"),\
                        dados_covid[59].alias("instalacoes_para_higienizacao"),\
                        dados_covid[60].alias("leitos_hospitalares_por_mil"),\
                        dados_covid[61].alias("expectativa_de_vida"),\
                        dados_covid[62].alias("indice_de_desenvolvimento_humano"),\
                        dados_covid[63].alias("excesso_de_mortalidade_cumulativa_absoluta"),\
                        dados_covid[64].alias("excesso_de_mortalidade_cumulativa"),\
                        dados_covid[65].alias("excesso_de_mortalidade"),\
                        dados_covid[66].alias("excesso_de_mortalidade_cumulativo_por_milhão"))   
                        
                      
                           
                    # ------------------------------------------------------------------------------------------
                    # Converte e lê arquivo para uma estrutura colunar e lê esses arquivos: 
                    # ------------------------------------------------------------------------------------------

                    dados_covid.write.parquet\
                    (r"D:\Curso BC8 Engenharia de Dados+Python\Visual Studio\Atividade Recesso\Arquivos_Parquet_casos_covid_novo")
                except Exception as e:
                    print("Erro ", str(e))    
            
            
           
            if option == "3":
                # ------------------------------------------------------------------------------------------
                # Quantidade de dados processados:
                # ------------------------------------------------------------------------------------------
                try:
                    print("-------------------------------------------------------------------------------------------------")
                    print(f'Há {dados_covid.count()} dados atualizados no dia 02/01/2021, FONTE: Our World in Data') 
                    print("-------------------------------------------------------------------------------------------------")        
                except Exception as e:
                    print("Erro ", str(e))
                    
            if option == "4":    
                try:
                    local = "China"
                    data = "2021-03-11"
                    
                    obitos_inicio_pandemia = dados_covid.groupBy('localizacao', 'data', 'novas_mortes')
                                                            
                    obitos_inicio_pandemia.filter((dados_covid['localizacao'] == local) & \
                                            (dados_covid['data'] == data)).show()
                except Exception as e:
                    print("Erro ", str(e))
                    
            if option == "5":    
                try:
                    local = "Brazil"
                    data = "2021-03-11"
                    
                    obitos_inicio_pandemia = dados_covid.groupBy('localizacao', 'data', 'novos casos')
                                                            
                    obitos_inicio_pandemia.filter((dados_covid['localizacao'] == local) & \
                                            (dados_covid['data'] == data)).show()
                except Exception as e:
                    print("Erro ", str(e))        
                    
            if option == "6":    
                try:
                    local = ""
                    data = "2021-03-11"
                    
                    obitos_inicio_pandemia = dados_covid.groupBy('localizacao', 'data', 'novos casos')
                                                            
                    obitos_inicio_pandemia.filter((dados_covid['localizacao'] == local) & \
                                            (dados_covid['data'] == data)).show()
                except Exception as e:
                    print("Erro ", str(e)) 
                            
            if option == "5":
                try:
                    # Instanceando as classes:
                    Interface_db_postgre = Interface_postgre('postgres', 'Matilde_10', '127.0.0.1', 'covid_cases')
                    Interface_db_cassandra = Interface_cassandra()
                    
                    # Lendo o arquivo csv:
                    df_covid = pd.read_csv('caso_covid_novo.csv')

                    # # Substitui dados vazios de todas as colunas  por 0.0 ou Null:
                    df_covid.update(df_covid['iso_code'].fillna("Null", inplace=True))
                    df_covid.update(df_covid['continent'].fillna("Null", inplace=True))
                    df_covid.update(df_covid['location'].fillna("Null", inplace=True))
                    df_covid.update(df_covid['date'].fillna("Null", inplace=True))
                    df_covid.update(df_covid['total_cases'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_cases'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_cases_smoothed'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['total_deaths'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_deaths'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_deaths_smoothed'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['total_cases_per_million'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_cases_per_million'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_cases_smoothed_per_million'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['total_deaths_per_million'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_deaths_per_million'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_deaths_smoothed_per_million'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['reproduction_rate'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['icu_patients'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['icu_patients_per_million'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['hosp_patients'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['hosp_patients_per_million'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['weekly_icu_admissions'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['weekly_icu_admissions_per_million'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['weekly_hosp_admissions'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['weekly_hosp_admissions_per_million'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_tests'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['total_tests'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['total_tests_per_thousand'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_tests_per_thousand'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_tests_smoothed'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_tests_smoothed_per_thousand'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['positive_rate'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['tests_per_case'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['tests_units'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['total_vaccinations'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['people_vaccinated'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['people_fully_vaccinated'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['total_boosters'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_vaccinations'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_vaccinations_smoothed'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['total_vaccinations_per_hundred'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['people_vaccinated_per_hundred'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['people_fully_vaccinated_per_hundred'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['total_boosters_per_hundred'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_vaccinations_smoothed_per_million'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_people_vaccinated_smoothed'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['new_people_vaccinated_smoothed_per_hundred'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['stringency_index'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['population'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['population_density'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['median_age'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['aged_65_older'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['aged_70_older'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['gdp_per_capita'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['extreme_poverty'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['cardiovasc_death_rate'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['diabetes_prevalence'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['female_smokers'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['male_smokers'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['handwashing_facilities'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['hospital_beds_per_thousand'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['life_expectancy'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['human_development_index'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['excess_mortality_cumulative_absolute'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['excess_mortality_cumulative'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['excess_mortality'].fillna(0.0, inplace=True))
                    df_covid.update(df_covid['excess_mortality_cumulative_per_million'].fillna(0.0, inplace=True))

                    
                                       
                    # Inseri dados do SQL no NoSQL:
                    columns_names = "id_covid,iso_code, continent, location, date, total_cases, new_cases, new_cases_smoothed, total_deaths, new_deaths, new_deaths_smoothed, total_cases_per_million, new_cases_per_million, new_cases_smoothed_per_million, total_deaths_per_million, new_deaths_per_million, new_deaths_smoothed_per_million, reproduction_rate, icu_patients, icu_patients_per_million, hosp_patients, hosp_patients_per_million, weekly_icu_admissions, weekly_icu_admissions_per_million, weekly_hosp_admissions, weekly_hosp_admissions_per_million, new_tests, total_tests, total_tests_per_thousand, new_tests_per_thousand, new_tests_smoothed, new_tests_smoothed_per_thousand, positive_rate, tests_per_case, tests_units, total_vaccinations, people_vaccinated, people_fully_vaccinated, total_boosters, new_vaccinations,new_vaccinations_smoothed, total_vaccinations_per_hundred, people_vaccinated_per_hundred, people_fully_vaccinated_per_hundred, total_boosters_per_hundred, new_vaccinations_smoothed_per_million, new_people_vaccinated_smoothed, new_people_vaccinated_smoothed_per_hundred, stringency_index, population, population_density, median_age, aged_65_older, aged_70_older, gdp_per_capita, extreme_poverty, cardiovasc_death_rate, diabetes_prevalence, female_smokers, male_smokers, handwashing_facilities, hospital_beds_per_thousand, life_expectancy, human_development_index, excess_mortality_cumulative_absolute, excess_mortality_cumulative, excess_mortality, excess_mortality_cumulative_per_million"
                    table_name = "covid_data"
                    for i in range(len(df_covid)):
                        data_to_insert = df_covid.iloc[i, 0], df_covid.iloc[i, 1], df_covid.iloc[i, 2],df_covid.iloc[i, 3], df_covid.iloc[i, 4], df_covid.iloc[i, 5],df_covid.iloc[i, 6], df_covid.iloc[i, 7], df_covid.iloc[i, 8],df_covid.iloc[i, 9], df_covid.iloc[i, 10], df_covid.iloc[i, 11],df_covid.iloc[i, 12], df_covid.iloc[i, 13], df_covid.iloc[i, 14],df_covid.iloc[i, 15], df_covid.iloc[i, 16], df_covid.iloc[i, 17],df_covid.iloc[i, 18], df_covid.iloc[i, 19], df_covid.iloc[i, 20],df_covid.iloc[i, 21], df_covid.iloc[i, 22], df_covid.iloc[i, 23],df_covid.iloc[i, 24], df_covid.iloc[i, 25], df_covid.iloc[i, 26],df_covid.iloc[i, 27], df_covid.iloc[i, 28], df_covid.iloc[i, 29],df_covid.iloc[i, 30], df_covid.iloc[i, 31], df_covid.iloc[i, 32],df_covid.iloc[i, 33], df_covid.iloc[i, 34], df_covid.iloc[i, 35],df_covid.iloc[i, 36], df_covid.iloc[i, 37], df_covid.iloc[i, 38],df_covid.iloc[i, 39], df_covid.iloc[i, 40], df_covid.iloc[i, 41],df_covid.iloc[i, 42], df_covid.iloc[i, 43], df_covid.iloc[i, 44],df_covid.iloc[i, 45], df_covid.iloc[i, 46], df_covid.iloc[i, 47],df_covid.iloc[i, 48], df_covid.iloc[i, 49], df_covid.iloc[i, 50],df_covid.iloc[i, 51], df_covid.iloc[i, 52], df_covid.iloc[i, 53],df_covid.iloc[i, 54], df_covid.iloc[i, 55], df_covid.iloc[i, 56],df_covid.iloc[i, 57], df_covid.iloc[i, 58], df_covid.iloc[i, 59],df_covid.iloc[i, 60], df_covid.iloc[i, 61], df_covid.iloc[i, 62],df_covid.iloc[i, 63], df_covid.iloc[i, 64], df_covid.iloc[i, 65], df_covid.iloc[i, 66], df_covid.iloc[i, 67]
                        data_insert = Interface_db_cassandra.insert_cassandra(table_name, columns_names, data_to_insert)
                except Exception as e:
                    print("Erro ao enviar dados do SQL para o NoSQL: ", str(e))


    except Exception as e:
        print("Erro ", str(e))