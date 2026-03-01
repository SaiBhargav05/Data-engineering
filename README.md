# Data Engineering Pipeline – MySQL to Postgres with Airflow & Docker

This project demonstrates a **production-style data engineering pipeline** that copies data from a **source MySQL database** to a **target PostgreSQL database**, orchestrated using **Apache Airflow** and containerized with **Docker**.

The goal of this project is to showcase **real-world data movement, orchestration, and infrastructure setup** commonly used in data engineering roles.

---

## Architecture Overview

- **Source Database**: MySQL  
- **Target Database**: PostgreSQL  
- **Orchestration**: Apache Airflow  
- **Containerization**: Docker  
- **Language**: Python  

---

## Prerequisites

Make sure you have the following installed:

- Docker  
- Docker Compose (optional but recommended)  
- Python 3.8+  
- pip  
- Git  

---

## Project Structure
.
├── app.py
├── Dockerfile
├── requirements.txt
├── airflow/
│ ├── dags/
│ ├── logs/
│ └── airflow.cfg
└── README.md


---

## Docker Setup

### Build Docker Image

```bash
docker build -t data-copier .
MySQL Setup (Source Database)

Run MySQL using Docker:

docker run \
  --name mysql_source \
  -e MYSQL_ROOT_PASSWORD=your_own_password \
  -e MYSQL_DATABASE=retail_db \
  -e MYSQL_USER=retail_user \
  -e MYSQL_PASSWORD=your_own_password \
  -d \
  -p 3306:3306 \
  mysql

Connect to MySQL:

docker exec -it mysql_source mysql -u retail_user -p
PostgreSQL Setup (Target Database)

Run PostgreSQL using Docker:

docker run \
  --name postgres_target \
  -e POSTGRES_DB=retail_db \
  -e POSTGRES_USER=retail_user \
  -e POSTGRES_PASSWORD=your_own_password \
  -d \
  -p 5432:5432 \
  postgres
Running the Application Using Docker
docker run --name data-copier \
  -v $(pwd):/app \
  -it \
  -e SOURCE_DB_USER=retail_user \
  -e SOURCE_DB_PASS=your_own_password \
  -e TARGET_DB_USER=retail_user \
  -e TARGET_DB_PASS=your_own_password \
  --entrypoint python \
  data-copier app.py dev departments
Apache Airflow Setup
Option 1: Airflow with SQLite (Development Only)
Steps
mkdir airflow
cd airflow
python -m venv airflow-env
source airflow-env/bin/activate
pip install apache-airflow

Initialize Airflow:

airflow initdb

Start services:

airflow webserver -p 8080 -D
airflow scheduler -D

Access UI at:

http://localhost:8080

Limitations

Not scalable

Suitable only for learning and development

Option 2: Airflow with MySQL (Production-like Setup)

Stop all running Airflow processes:

cat airflow-scheduler.pid | xargs kill
cat airflow-webserver.pid | xargs kill
ps -ef | grep airflow

Install MySQL connector:

pip install mysql-connector-python

Run MySQL for Airflow metadata:

docker run \
  --name mysql_airflow \
  -e MYSQL_ROOT_PASSWORD=your_own_password \
  -d \
  -p 4306:3306 \
  mysql

Create Airflow database:

CREATE DATABASE airflow;
CREATE USER airflow IDENTIFIED BY 'your_own_password';
GRANT ALL ON airflow.* TO airflow;
FLUSH PRIVILEGES;

Update airflow.cfg:

executor = LocalExecutor
sql_alchemy_conn = mysql+mysqlconnector://airflow:your_own_password@localhost:4306/airflow?use_pure=True

Tune concurrency:

parallelism = 8
dag_concurrency = 4
max_active_runs_per_dag = 4

Initialize DB and start services:

airflow initdb
airflow webserver -p 8080 -D
airflow scheduler -D
Using DockerOperator in Airflow

Install Docker support:

pip install apache-airflow[docker]

This allows Airflow to run your data pipeline inside Docker containers using DockerOperator.

Key Learnings from This Project

End-to-end data movement between heterogeneous databases

Environment-variable based credential handling

Airflow executor configurations

Dockerized data pipelines

Production-style data engineering workflows

Future Improvements

Add Docker Compose for one-command setup

Add data validation checks

Add retry logic and alerting

Add CI/CD pipeline

Migrate to CeleryExecutor

