"""
file: parquet_analyzer.py
brief:
author: S. V. Paulauskas
date: November 20, 2020
"""
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# DATA_FILE = "D:/projects/dolosse/dolosse/analysis/PldToParquet/data/single-spill.parquet"
# DATA_FILE = "D:/projects/dolosse/dolosse/analysis/PldToParquet/data/runBaGeL_337.parquet"
DATA_FILE = 'D:/projects/dolosse/dolosse/analysis/PldToParquet/data/runPR270_406.parquet'

spark_conf = SparkConf().setAppName("parquet_analyzer").setMaster('local[*]')

spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()

df = spark.read.parquet(DATA_FILE)

pdf = df.where((col('slot') == 2) & (col('channel') == 0) & (col('energy') > 0)).select(
    "energy").toPandas()
for plt in pdf.hist(bins=2000, range=[0, 2000]).flatten():
    # plt.set_xlabel('Channel')
    # plt.set_ylabel('Counts /  Channel')
    plt.set_yscale('log')
    # plt.title("Energy ")
    plt.get_figure().show()
