import argparse
import os
import shutil
import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, date_format, sum as soma, window
from pyspark.sql.types import BooleanType, StringType, StructField, StructType, TimestampType

from config import (
    FORMATO_DATA_HORA,
    PASTA_CHECKPOINT,
    PASTA_ENTRADA,
    PASTA_PUBLICACAO,
    PASTA_STREAMING,
    SINAL_CONSUMIDOR_PRONTO,
)

ESQUEMA_NOTIFICACAO = StructType([
    StructField("id_notificacao", StringType()),
    StructField("dt_notificacao", TimestampType()),
    StructField("uf_residencia", StringType()),
    StructField("regiao_residencia", StringType()),
    StructField("classificacao_final", StringType()),
    StructField("caso_grave", BooleanType()),
])


def preparar_pastas():
    shutil.rmtree(PASTA_STREAMING, ignore_errors=True)
    PASTA_ENTRADA.mkdir(parents=True)
    PASTA_PUBLICACAO.mkdir()


def iniciar_spark():
    os.environ["PYSPARK_PYTHON"] = sys.executable
    os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
    spark = (
        SparkSession.builder.master("local[2]")
        .appName("Dengue 2026: consumidor de notificações")
        .config("spark.sql.shuffle.partitions", "2")
        .config("spark.sql.session.timeZone", "UTC")
        .config("spark.ui.showConsoleProgress", "false")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("ERROR")
    return spark


def iniciar_consulta(spark):
    notificacoes = (
        spark.readStream
        .schema(ESQUEMA_NOTIFICACAO)
        .option("timestampFormat", FORMATO_DATA_HORA)
        .option("maxFilesPerTrigger", 1)
        .json(str(PASTA_ENTRADA))
    )
    por_janela = (
        notificacoes
        .groupBy(window("dt_notificacao", "1 day").alias("janela"), "regiao_residencia")
        .agg(
            count("*").alias("notificacoes"),
            soma(col("caso_grave").cast("int")).alias("casos_graves"),
        )
        .select(
            date_format("janela.start", "dd/MM HH:mm").alias("inicio"),
            date_format("janela.end", "dd/MM HH:mm").alias("fim"),
            col("regiao_residencia").alias("regiao"),
            "notificacoes",
            "casos_graves",
        )
        .orderBy("inicio", "regiao")
    )
    return (
        por_janela.writeStream
        .format("console")
        .outputMode("complete")
        .option("truncate", "false")
        .option("numRows", 100)
        .option("checkpointLocation", str(PASTA_CHECKPOINT))
        .trigger(processingTime="2 seconds")
        .start()
    )


def main():
    argumentos = argparse.ArgumentParser(description="Consome notificações de dengue em streaming com janela tumbling de 1 dia.")
    argumentos.add_argument("--duracao", type=float, default=None, help="segundos até encerrar; sem valor, roda até Ctrl+C")
    duracao = argumentos.parse_args().duracao

    preparar_pastas()
    spark = iniciar_spark()
    consulta = iniciar_consulta(spark)
    SINAL_CONSUMIDOR_PRONTO.touch()
    print(f"Consumidor pronto. Monitorando {PASTA_ENTRADA}", flush=True)
    print("Janela tumbling de 1 dia sobre dt_notificacao, por região. Ctrl+C encerra.", flush=True)
    try:
        consulta.awaitTermination(duracao)
    except KeyboardInterrupt:
        pass
    finally:
        consulta.stop()
        spark.stop()
        SINAL_CONSUMIDOR_PRONTO.unlink(missing_ok=True)
        print("Consumidor encerrado.", flush=True)


if __name__ == "__main__":
    main()
