from pyspark.sql import SparkSession
import os
os.environ["PYSPARK_PYTHON"] = "C:/Users/2446_/AppData/Local/Programs/Python/Python39/python.exe"


# Spark 세션 시작
spark = SparkSession.builder.appName('Spark Test').getOrCreate()

# Spark 버전 확인
print(f"Spark version: {spark.version}")

# 간단한 DataFrame 생성
data = [("John", "Doe", 30), ("Jane", "Doe", 25), ("Mike", "Jordan", 35)]
columns = ["First Name", "Last Name", "Age"]

df = spark.createDataFrame(data, columns)

# DataFrame 출력
df.show()

# 세션 종료
spark.stop()
