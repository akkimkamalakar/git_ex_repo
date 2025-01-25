from pyspark.sql import SparkSession
spark=SparkSession.builder.getOrCreate()

df=spark.read.csv('s3://this is s3 path')
df.show()

df2=spark.read.csv('s3//pth2')

df3=df.join(df2,how='inner',on='df.id')
print(spark)