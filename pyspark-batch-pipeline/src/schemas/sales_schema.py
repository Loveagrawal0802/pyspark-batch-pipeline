
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType

sales_schema = StructType([
    StructField("transaction_id", StringType(), True),
    StructField("customer_id", StringType(), True),
    StructField("product_category", StringType(), True),
    StructField("amount", DoubleType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("transaction_date", StringType(), True)
])
