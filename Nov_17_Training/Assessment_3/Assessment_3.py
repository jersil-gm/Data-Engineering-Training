import csv
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


def load_baggage():
    with open('/opt/airflow/dags/airport_baggage.csv', newline='') as file:
        records = list(csv.DictReader(file))
    print('Baggage records loaded:', len(records))
    return records


def identify_review_bags(ti):
    records = ti.xcom_pull(task_ids='load_baggage')
    review_bags = []
    for bag in records:
        weight_kg = int(bag['weight_kg'])
        status = bag['screening_status']
        if status == 'Review' or weight_kg > 23:
            review_bags.append(bag['bag_id'])
    print('Bag IDs requiring review:', review_bags)
    return review_bags


def calculate_total_weight(ti):
    records = ti.xcom_pull(task_ids='load_baggage')
    total_weight = 0
    for bag in records:
        total_weight += int(bag['weight_kg'])
    print('Total baggage weight (kg):', total_weight)
    return total_weight


def generate_report(ti):
    records = ti.xcom_pull(task_ids='load_baggage')
    review_bags = ti.xcom_pull(task_ids='identify_review_bags')
    total_weight = ti.xcom_pull(task_ids='calculate_total_weight')

    print('=== AIRPORT BAGGAGE SCREENING REPORT ===')
    print(f'Total number of bags: {len(records)}')
    print(f"Bag IDs requiring review: {', '.join(review_bags) if review_bags else 'None'}")
    print(f'Total baggage weight: {total_weight} kg')
    print('========================================')


with DAG(
    dag_id='airport_baggage_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=['airport', 'assessment'],
) as dag:

    task_load_baggage = PythonOperator(
        task_id='load_baggage',
        python_callable=load_baggage,
    )

    task_identify_review_bags = PythonOperator(
        task_id='identify_review_bags',
        python_callable=identify_review_bags,
    )

    task_calculate_total_weight = PythonOperator(
        task_id='calculate_total_weight',
        python_callable=calculate_total_weight,
    )

    task_generate_report = PythonOperator(
        task_id='generate_report',
        python_callable=generate_report,
    )

    # Parallel branching dependency
    task_load_baggage >> [task_identify_review_bags, task_calculate_total_weight] >> task_generate_report
