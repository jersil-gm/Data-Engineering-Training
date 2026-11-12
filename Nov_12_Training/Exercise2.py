from airflow import DAG
from airflow.providers.standard.operators.python import (
    PythonOperator,
    BranchPythonOperator
)
from datetime import datetime, timedelta


def load_incident():
    incident = {
        "ticket_id": "INC-402",
        "service": "Email",
        "severity": "High",
        "reported_by": "Operations"
    }
    print("Loaded incident:", incident)
    return incident


def choose_response(**context):
    incident = context["ti"].xcom_pull(task_ids="load_incident")
    severity = incident.get("severity", "").lower()

    if severity in ["high", "critical"]:
        print(f"Severity is {incident['severity']} -> Routing to urgent_response")
        return "urgent_response"
    else:
        print(f"Severity is {incident['severity']} -> Routing to standard_response")
        return "standard_response"


def urgent_response(**context):
    incident = context["ti"].xcom_pull(task_ids="load_incident")
    attempt = context["ti"].try_number

    if attempt == 1:
        print(f"Attempt {attempt}: Escalation service temporarily unavailable!")
        raise RuntimeError("Simulated temporary failure on first attempt.")

    print(f"Attempt {attempt}: URGENT ESCALATION triggered for {incident['ticket_id']} ({incident['service']})!")


def standard_response(**context):
    incident = context["ti"].xcom_pull(task_ids="load_incident")
    print(f"Standard service-desk ticket assigned for {incident['ticket_id']} ({incident['service']}).")


def write_audit(**context):
    incident = context["ti"].xcom_pull(task_ids="load_incident")
    print(f"AUDIT LOG: Incident {incident['ticket_id']} routing completed successfully.")


with DAG(
    dag_id="it_incident_priority_routing",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    t_load = PythonOperator(
        task_id="load_incident",
        python_callable=load_incident
    )

    t_branch = BranchPythonOperator(
        task_id="choose_response",
        python_callable=choose_response
    )

    t_urgent = PythonOperator(
        task_id="urgent_response",
        python_callable=urgent_response,
        retries=1,
        retry_delay=timedelta(seconds=5)
    )

    t_standard = PythonOperator(
        task_id="standard_response",
        python_callable=standard_response
    )

    t_audit = PythonOperator(
        task_id="write_audit",
        python_callable=write_audit,
        trigger_rule="none_failed_min_one_success"
    )

    t_load >> t_branch >> [t_urgent, t_standard] >> t_audit
