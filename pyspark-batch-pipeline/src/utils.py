import os
import tempfile
from pyspark.sql import SparkSession

def get_spark_session(app_name="PySparkBatchPipeline"):
    # Create a temporary directory in Python to satisfy Spark's folder requirement
    temp_dir = tempfile.mkdtemp()
    
    if "HADOOP_HOME" not in os.environ:
        os.environ["HADOOP_HOME"] = temp_dir

    return SparkSession.builder \
        .appName(app_name) \
        .master("local[*]") \
        .config("spark.driver.host", "localhost") \
        .config("spark.sql.shuffle.partitions", "2") \
        .config("spark.hadoop.fs.defaultFS", "file:///") \
        .getOrCreate()