import os
import tempfile

# Dummy environment variables so Spark initializes without throwing Hadoop warnings
temp_dir = tempfile.mkdtemp()
os.environ["HADOOP_HOME"] = temp_dir

from src.utils import get_spark_session
from src.schemas.sales_schema import sales_schema
from src.ingestion import load_sales_data
from src.transformations import clean_and_filter_data, compute_business_metrics

def run_pipeline():
    # 1. Start PySpark session
    spark = get_spark_session()
    
    # 2. Ingest CSV
    sales_df = load_sales_data(
        spark=spark, 
        file_path="data/raw/sales_part1.csv", 
        file_format="csv", 
        schema=sales_schema
    )
    
    # 3. Clean & Transform using PySpark & Spark SQL
    filtered_df = clean_and_filter_data(sales_df)
    metrics_df = compute_business_metrics(filtered_df)
    
    # 4. Display result in terminal
    print("\n--- AGGREGATED BUSINESS METRICS ---")
    metrics_df.show()
    print("-----------------------------------\n")
    
    # 5. Save output without Hadoop (Convert Spark DF -> Pandas -> CSV)
    os.makedirs("data/output", exist_ok=True)
    pandas_df = metrics_df.toPandas()
    pandas_df.to_csv("data/output/business_metrics_report.csv", index=False)
    
    print("Pipeline executed successfully!")

if __name__ == "__main__":
    run_pipeline()