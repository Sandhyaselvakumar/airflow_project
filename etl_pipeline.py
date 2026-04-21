from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import pandas as pd
import sqlite3

# -----------------------------
# 1. Extract Task
# -----------------------------
def extract():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data)
    df.to_csv("/tmp/raw_data.csv", index=False)

    print("Extracted data successfully")


# -----------------------------
# 2. Transform Task
# -----------------------------
def transform():
    df = pd.read_csv("/tmp/raw_data.csv")

    df = df[["userId", "id", "title"]]
    df.columns = ["user_id", "post_id", "title"]

    df.drop_duplicates(inplace=True)

    df.to_csv("/tmp/clean_data.csv", index=False)

    print("Transformed data successfully")


# -----------------------------
# 3. Load Task
# -----------------------------
def load():
    df = pd.read_csv("/tmp/clean_data.csv")

    db_path = "/home/sandhya/airflow/mydb.db"

    print("Saving database to:", db_path)

    conn = sqlite3.connect(db_path)

    df.to_sql("posts", conn, if_exists="replace", index=False)

    conn.close()

    print("Database saved successfully!")


# -----------------------------
# DAG Definition
# -----------------------------
default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
    "retries": 1
}

dag = DAG(
    "simple_etl_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
)

# -----------------------------
# Tasks
# -----------------------------
extract_task = PythonOperator(
    task_id="extract",
    python_callable=extract,
    dag=dag
)

transform_task = PythonOperator(
    task_id="transform",
    python_callable=transform,
    dag=dag
)

load_task = PythonOperator(
    task_id="load",
    python_callable=load,
    dag=dag
)

# -----------------------------
# Task Order
# -----------------------------
extract_task >> transform_task >> load_task
