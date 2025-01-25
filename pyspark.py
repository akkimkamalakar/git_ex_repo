from pyspark.sql import SparkSession
spark=SparkSession.builder.getOrCreate()

df=spark.read.csv('s3://this is s3 path')
df.show()
print(spark)