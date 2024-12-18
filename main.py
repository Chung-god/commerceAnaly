import pyspark
from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder \
    .master("local") \
    .appName("PySpark Installation Check") \
    .getOrCreate()

# Spark 세션 버전 확인
print(spark.version)

# 간단한 데이터프레임 생성
data = [("Alice", "Brown"), ("Bob", "Smith")]
df = spark.createDataFrame(data, ["First Name", "Last Name"])
df.show()

# Spark 세션 종료
spark.stop()