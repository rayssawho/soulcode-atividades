# CONVERSAO DA VIRGULA PARA PONTO <<<< essa forma funcionou com todas as colunas
 viagens = viagens.withColumn("Valor_diarias",B.regexp_replace("Valor_diarias",",","."))
 viagens = viagens.withColumn("Valor_passagens",B.regexp_replace("Valor_passagens",",","."))
 viagens = viagens.withColumn("Outros_gastos",B.regexp_replace("Outros_gastos",",","."))
 viagens.show()


# MUDANDO O TIPO PARA FloatType
 viagens = viagens.withColumn("Valor_passagens",B.col("Valor_passagens").cast(FloatType()))
 viagens = viagens.withColumn("Valor_diarias",B.col("Valor_diarias").cast(FloatType()))
 viagens = viagens.withColumn("Outros_gastos",B.col("Outros_gastos").cast(FloatType()))
 viagens.printSchema()


