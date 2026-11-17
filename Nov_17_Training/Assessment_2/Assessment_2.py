import csv
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


def load_atms():
    with open('/opt/airflow/dags/atm_cash.csv', newline='') as file:
        records = list(csv.DictReader(file))
    print('ATM records loaded:', len(records))
    return records


def identify_low_cash(ti):
    records = ti.xcom_pull(task_ids='load_atms')
    low_cash_atms = []
    for atm in records:
        cash_available = int(atm['cash_available'])
        daily_demand = int(atm['daily_demand'])
        if cash_available < daily_demand:
            low_cash_atms.append(atm['atm_id'])
    print('Low-cash ATM IDs:', low_cash_atms)
    return low_cash_atms


def calculate_total_cash(ti):
    records = ti.xcom_pull(task_ids='load_atms')
    total_cash = 0
    for atm in records:
        total_cash += int(atm['cash_available'])
    print('Total available cash:', total_cash)
    return total_cash


def generate_report(ti):
    records = ti.xcom_pull(task_ids='load_atms')
    low_cash_atms = ti.xcom_pull(task_ids='identify_low_cash')
    total_cash = ti.xcom_pull(task_ids='calculate_total_cash')

    print('=== ATM CASH REPLENISHMENT REPORT ===')
    print(f'Total number of ATMs: {len(records)}')
    print(f"Low-cash ATM IDs: {', '.join(low_cash_atms) if low_cash_atms else 'None'}")
    print(f'Total available cash: ${total_cash:,}')
    print('=====================================')


with DAG(
    dag_id='atm_cash_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=['banking', 'assessment'],
) as dag:

    task_load_atms = PythonOperator(
        task_id='load_atms',
        python_callable=load_atms,
    )

    task_identify_low_cash = PythonOperator(
        task_id='identify_low_cash',
        python_callable=identify_low_cash,
    )

    task_calculate_total_cash = PythonOperator(
        task_id='calculate_total_cash',
        python_callable=calculate_total_cash,
    )

    task_generate_report = PythonOperator(
        task_id='generate_report',
        python_callable=generate_report,
    )

    # Parallel branching dependency
    task_load_atms >> [task_identify_low_cash, task_calculate_total_cash] >> task_generate_report
