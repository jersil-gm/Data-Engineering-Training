import csv
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


def load_batches():
    with open("/opt/airflow/dags/factory_batches.csv", newline="") as file:
        rows = list(csv.DictReader(file))
    print("Batches loaded:", len(rows))
    return rows


def check_quality(ti):
    batches = ti.xcom_pull(task_ids="load_batches")
    review_batches = []
    for batch in batches:
        units = int(batch["units_produced"])
        defects = int(batch["defective_units"])
        if units > 0 and (defects / units) > 0.05:
            review_batches.append(batch["batch_id"])
    print("Batches requiring quality review:", review_batches)
    return review_batches


def calculate_value(ti):
    batches = ti.xcom_pull(task_ids="load_batches")
    total_value = 0
    for batch in batches:
        units = int(batch["units_produced"])
        value_per_unit = int(batch["value_per_unit"])
        total_value += units * value_per_unit
    print("Total production value:", total_value)
    return total_value


def generate_report(ti):
    batches = ti.xcom_pull(task_ids="load_batches")
    review_batches = ti.xcom_pull(task_ids="check_quality")
    total_value = ti.xcom_pull(task_ids="calculate_value")

    print("=== MANUFACTURING BATCH QUALITY REPORT ===")
    print(f"Total number of batches: {len(batches)}")
    print(f"Batch IDs requiring review (>5% defects): {', '.join(review_batches) if review_batches else 'None'}")
    print(f"Total production value: ${total_value:,}")
    print("==========================================")


with DAG(
    dag_id="factory_quality_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["manufacturing", "assessment"],
) as dag:

    task_load_batches = PythonOperator(
        task_id="load_batches",
        python_callable=load_batches,
    )

    task_check_quality = PythonOperator(
        task_id="check_quality",
        python_callable=check_quality,
    )

    task_calculate_value = PythonOperator(
        task_id="calculate_value",
        python_callable=calculate_value,
    )

    task_generate_report = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report,
    )

    # Parallel branching dependency
    task_load_batches >> [task_check_quality, task_calculate_value] >> task_generate_report


