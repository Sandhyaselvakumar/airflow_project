# 🚀 Airflow ETL Pipeline Project

## 📌 Overview

This project demonstrates a simple **ETL (Extract, Transform, Load) pipeline** built using **Apache Airflow**.

The pipeline:

* Extracts data from a public API
* Transforms and cleans the data using Pandas
* Loads the processed data into a SQLite database

---

## 🏗️ Architecture

```
API → Extract → Transform → Load → SQLite Database
```

---

## 🔧 Technologies Used

* Apache Airflow
* Python
* Pandas
* SQLite
* REST API (JSONPlaceholder)

---

## ⚙️ DAG Details

* **DAG ID:** `simple_etl_pipeline`
* **Schedule:** Daily (`@daily`)
* **Tasks:**

  * `extract`
  * `transform`
  * `load`

---

## 🔄 Pipeline Steps

### 1. Extract

* Fetches data from:

  ```
  https://jsonplaceholder.typicode.com/posts
  ```
* Converts JSON to DataFrame
* Saves raw data to:

  ```
  /tmp/raw_data.csv
  ```

---

### 2. Transform

* Reads raw CSV
* Selects relevant columns:

  * userId → user_id
  * id → post_id
  * title
* Removes duplicates
* Saves cleaned data to:

  ```
  /tmp/clean_data.csv
  ```

---

### 3. Load

* Loads cleaned data into SQLite database:

  ```
  /home/sandhya/airflow/mydb.db
  ```
* Table name:

  ```
  posts
  ```

---

## 🗃️ Database Schema

| Column  | Description     |
| ------- | --------------- |
| user_id | User identifier |
| post_id | Post identifier |
| title   | Post title      |

---

## ▶️ How to Run

### 1. Start Airflow

```bash
airflow webserver --port 8080
airflow scheduler
```

---

### 2. Open UI

```
http://localhost:8080
```

---

### 3. Run DAG

* Enable DAG
* Click ▶️ to trigger

---

## 🔍 Data Verification

### Using Python

```python
import sqlite3

conn = sqlite3.connect("/home/sandhya/airflow/mydb.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM posts LIMIT 5;")
print(cursor.fetchall())

conn.close()
```

---

### Using SQL

```sql
SELECT * FROM posts LIMIT 5;
```

---

## 📊 Sample Queries

```sql
-- Count total rows
SELECT COUNT(*) FROM posts;

-- Group by user
SELECT user_id, COUNT(*) FROM posts GROUP BY user_id;

-- Latest posts
SELECT * FROM posts ORDER BY post_id DESC LIMIT 5;
```

---

## ⚠️ Notes

* `/tmp` is a temporary directory used for intermediate data
* Current pipeline overwrites data (`replace` mode)
* Can be modified to `append` for historical storage

---

## 🚀 Future Improvements

* Use PostgreSQL instead of SQLite
* Add Docker support
* Implement data validation checks
* Add logging & monitoring
* Schedule incremental loads

---

## 🎯 Key Learnings

* Building ETL pipelines with Airflow
* Task orchestration using DAGs
* Debugging using Airflow logs
* Handling file paths in distributed systems
* SQL-based data validation

---

## 💡 Author

**Sandhya**

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
