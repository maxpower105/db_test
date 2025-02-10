from pyspark.sql import SparkSession, DataFrame

def get_sm(spark: SparkSession) -> DataFrame:
    """
    Fetches data from the Databricks table `lwmscanmasterdatav2`
    in the `operations_dev.manufacturing_staging` schema.
    """
    return spark.read.table("operations_dev.manufacturing_staging.lwmscanmasterdatav2")

def get_lwm(spark: SparkSession) -> DataFrame:
    """
    Fetches data from the Databricks table `lwmssqldatav2`
    in the `operations_dev.manufacturing_staging` schema.
    """
    return spark.read.table("operations_dev.manufacturing_staging.lwmssqldatav2")

def get_spark() -> SparkSession:
    """
    Initializes a Spark session, using Databricks Connect if available.
    """
    try:
        from databricks.connect import DatabricksSession
        return DatabricksSession.builder.getOrCreate()
    except ImportError:
        return SparkSession.builder.appName("Databricks_Connector").getOrCreate()

def main():
    """
    Main function to fetch data from Databricks and display the first 5 rows.
    """
    spark = get_spark()  # Get the Spark session
    df_sm = get_sm(spark)  # Fetch sm data
    df_lwm = get_lwm(spark)  # Fetch lwm data 
    df_sm.show(5)  # Display first 5 rows
    df_lwm.show(5)  # Display first 5 rows

if __name__ == '__main__':
    main()
