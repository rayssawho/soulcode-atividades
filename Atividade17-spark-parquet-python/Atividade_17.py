from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import functions as B
from pyspark.sql.types import FloatType
import pandas as pd

spark = (
    SparkSession.builder.appName("OTR")
    .config("spark.sql.caseSensitive", "True")
    .getOrCreate()
)

# IMPORTANDO OS ARQUIVOS CSV
viagem2020 = (
    spark.read.format("csv")
    .option("header", "true")
    .option("delimiter", ";")
    .option("inferSchema", "true")
    .option("encoding", "ISO-8859-1")
    .load(r".\dados\2020_Viagem.csv")
)
viagem2021 = (
    spark.read.format("csv")
    .option("header", "true")
    .option("delimiter", ";")
    .option("inferSchema", "true")
    .option("encoding", "ISO-8859-1")
    .load(r".\dados\2021_Viagem.csv")
)

# UNINDO
viagens = viagem2020.union(viagem2021)

# MUDANÇA NOME DAS COLUNAS
viagens = viagens.select(
    viagens["Identificador do processo de viagem"].alias("id_processo"),
    viagens["Situação"].alias("Situacao"),
    viagens["Viagem Urgente"].alias("Viagem_urgente"),
    viagens["Justificativa Urgência Viagem"].alias("Justificativa"),
    viagens["Nome órgão solicitante"].alias("Orgao_solicitante"),
    viagens["Nome"].alias("Solicitante"),
    viagens["Cargo"].alias("Cargo"),
    viagens["Período - Data de início"].alias("Data_inicio"),
    viagens["Período - Data de fim"].alias("Data_fim"),
    viagens["Destinos"].alias("Destinos"),
    viagens["Motivo"].alias("Motivo"),
    viagens["Valor diárias"].alias("Valor_diarias"),
    viagens["Valor passagens"].alias("Valor_passagens"),
    viagens["Valor outros gastos"].alias("Outros_gastos"),
)
viagens.printSchema()

# CONVERSÃO PARA PARQUET
viagens.write.parquet(
    r".\Parquet_Ativ_17"
)
viagens = spark.read.parquet(
    r".\Parquet_Ativ_17"
)
viagens.printSchema()

# CONVERSÃO DA VIRGULA PARA PONTO


def converter_valor(variavel):
    return float(variavel.replace(",", "."))


udf_converter_valor = B.udf(converter_valor, FloatType())
viagens1 = (
    viagens.withColumn("Valor_diarias", udf_converter_valor(viagens["Valor_diarias"]))
    .withColumn("Valor_passagens", udf_converter_valor(viagens["Valor_passagens"]))
    .withColumn("Outros_gastos", udf_converter_valor(viagens["Outros_gastos"]))
)
viagens1.printSchema()
# viagens1.show()
