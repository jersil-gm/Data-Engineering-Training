import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, hour, when, sum as _sum, round

# 1. Start Spark Session
spark = SparkSession.builder \
    .appName("SmartHomeEnergy") \
    .master("local[*]") \
    .getOrCreate()

# 2. File paths
current_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(current_dir, "..", "data", "large_sensor_logs.csv")
output_csv = os.path.join(current_dir, "output_top_devices.csv")

# 3. Read CSV data
df = spark.read.csv(input_file, header=True, inferSchema=True)
print("\n--- Raw Sensor Data Sample ---")
df.show(5)

# 4. Classify Peak (06:00 to 22:00) vs Off-Peak
df = df.withColumn("reading_hour", hour(col("timestamp")))
df = df.withColumn(
    "time_of_day",
    when((col("reading_hour") >= 6) & (col("reading_hour") < 22), "PEAK").otherwise("OFF_PEAK")
)

# 5. Calculate Total Energy per Device
top_devices = df.groupBy("device_id", "device_type") \
    .agg(round(_sum("energy_kwh"), 2).alias("total_kwh")) \
    .orderBy(col("total_kwh").desc())

print("\n--- Top Energy Consuming Devices ---")
top_devices.show()

# 6. Peak vs Off-Peak Summary per Device
peak_summary = df.groupBy("device_id", "time_of_day") \
    .agg(round(_sum("energy_kwh"), 2).alias("kwh")) \
    .orderBy("device_id")

print("\n--- Usage Breakdown by Peak / Off-Peak ---")
peak_summary.show()

# 7. Save output cleanly (avoids Windows Hadoop winutils error)
top_devices_pd = top_devices.toPandas()
top_devices_pd.to_csv(output_csv, index=False)
print(f"\nSaved top devices summary to: {output_csv}")

# 8. Stop Spark
spark.stop()