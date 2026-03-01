# Data Engineering Pipeline: MySQL to PostgreSQL Migration

## 📌 Project Overview
This project implements a robust, automated Data Engineering pipeline designed to migrate data from a **MySQL** source to a **PostgreSQL** target. Orchestrated by **Apache Airflow** and executed via **Docker**, the pipeline ensures environment-agnostic execution and scalable data movement.

The primary use case is the synchronization of relational database tables (such as `customers`, `orders`, and `products`) across different database technologies.

---

## 🏗 System Architecture
- **Orchestration**: Apache Airflow manages task scheduling and monitoring.
- **Execution**: A custom Docker container (`data-copier-live`) isolates the Python ETL logic.
- **Storage**: Data extraction from MySQL and loading into PostgreSQL.



---

## 📂 Repository Breakdown

| File | Role |
| :--- | :--- |
| **`app.py`** | The core Python ETL script using SQLAlchemy and Pandas. |
| **`data-copier-docker.py`** | The Airflow DAG using `DockerOperator`. |
| **`Dockerfile`** | Defines the environment (Python, Drivers, Libraries). |
| **`requirements.txt`** | Python dependencies (SQLAlchemy, mysql-connector, psycopg2). |

---

## 🚀 Getting Started

### 1. Build the Docker Image
Run this in your terminal (Linux or WSL) from the project root:
```bash
docker build -t data-copier-live:latest .
