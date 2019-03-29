# Databricks notebook source
# Chapter 6. Working with Different Types of Data

# COMMAND ----------

# 데이터 불러오기
# File location and type
file_location = "/FileStore/tables/2010_12_01-ec65d.csv"
file_type = "csv"

# CSV options
infer_schema = "true"
first_row_is_header = "true"
delimiter = ","

# The applied options are for CSV files. For other file types, these will be ignored.
df = spark.read.format(file_type) \
  .option("inferSchema", infer_schema) \
  .option("header", first_row_is_header) \
  .option("sep", delimiter) \
  .load(file_location)


df.createOrReplaceTempView("dfTable") # df에 불러놓은 데이터를 뷰로 만들어줌 --> 나중에 SQL 문으로 쿼리 가능
display(df)

# COMMAND ----------

df.printSchema()

# COMMAND ----------



# COMMAND ----------

# Converting to Spark Types ------------------------------------------------------------------------------------
from pyspark.sql.functions import lit
df.select(lit(5), lit("five"), lit(5.0)  #? 이게 머여.. 

# COMMAND ----------

# Working with booleans ------------------------------------------------------------------------------------
from pyspark.sql.functions import col

df.where(col("InvoiceNo") !=536365)\
.select("InvoiceNo", "Description")\
.show(5, False)

# COMMAND ----------

# df.where("InvoiceNo = 536365").show(5, False)
df.where("Quantity <> 6").show(5, False) # <>는 !=랑 같은 개념. 

# COMMAND ----------

# Filtering : or / and로 boolean statement 묶어주기
from pyspark.sql.functions import instr

# -- 방법 1: boolen expression 사용하기
priceFilter = col("UnitPrice") > 600
descripFilter = instr(df.Description, "POSTAGE") >=1
df.where(col("StockCode").isin("DOT")).where(priceFilter | descripFilter).show()

# COMMAND ----------

#%sql
-- in sql
SELECT * FROM dfTable WHERE StockCode in ("DOT") AND (UnitPrice > 600 OR instr(Description, "POSTAGE")>=1)

# COMMAND ----------

# -- 방법 2 : Boolen 칼럼 만들기 
DOTCodeFilter = col("StockCode") == 'DOT'
priceFilter = col("UnitPrice")>600
descripFilter = instr(col("Description"), "POSTAGE") >= 1

df.withColumn("isExpensive", DOTCodeFilter & (priceFilter|descripFilter)).where('isExpensive').select("unitPrice", "isExpensive").show(5)

# COMMAND ----------

# 칼럼을 만들때, boolean expression이 아니라 SQL statement를 활용할 수도 있음!
from pyspark.sql.functions import expr
df.withColumn("isExpensive", expr("NOT Unitprice <= 250")).where("isExpensive").select("isExpensive","Description", "UnitPrice").show(5)

# COMMAND ----------

# 그런데 데이터에 Null이 있다면?  Equality test that is safe for null values.
df.where(col("Description")!="Hello").show()

# COMMAND ----------

# 그런데 데이터에 Null이 있다면?  eqNullSafe : Equality test that is safe for null values.
df.where(col("Description").eqNullSafe("Hello")).show()

# COMMAND ----------

df.filter(df.quantity.isNull()).show()

# COMMAND ----------

# Working with Numbers! ----------------------------------------------------- 
from pyspark.sql.functions import expr, pow

########## POWER ############
fabricatedQuantity = pow(col("Quantity")*col("UnitPrice"), 2) +5 # Returns the value of the first argument raised to the power of the second argument.
df.select(expr("CustomerId"), fabricatedQuantity.alias("realQuantity")).show(2)

# COMMAND ----------

# selectExpr 을 사용해서 SQL 스타일로 쓸 수도 있음!
df.selectExpr("CustomerId", "(POWER((Quantity * UnitPrice), 2.0)+5) as realQuantity").show(2)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT customerId, (POWER((Quantity*UnitPrice),2)+5) as realQuantity FROM dfTable Limit 2

# COMMAND ----------

########## Rounding ############
from pyspark.sql.functions import lit, round, bround

# COMMAND ----------

df.select(round(lit("2.5")), bround(lit("2.5"))).show(2)

# COMMAND ----------

########## Correlation ############
from pyspark.sql.functions import corr
df.stat.corr("Quantity", "UnitPrice")
df.select(corr("Quantity", "UnitPrice")).show()

# COMMAND ----------

########## Stats ############
from pyspark.sql.functions import count, mean, stddev_pop, min, max

df.describe().show()

# COMMAND ----------

# == Approximate quantiles
colName = "UnitPrice"
quantileProbs = [0.5]
relError = 0.05
df.stat.approxQuantile("UnitPrice", quantileProbs, relError)

# COMMAND ----------

df.select(col("StockCode"), col("Quantity")).show(4)

# COMMAND ----------

# df.stat.crosstab("StockCode", "Quantity").show()
df.stat.freqItems(["StockCode", "Quantity"]).show()

# COMMAND ----------

df.select(monotonically_increasing_id()).show(2)
