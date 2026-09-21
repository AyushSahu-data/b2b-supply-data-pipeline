# HENDI B2B Data Pipeline: Automated ELT & Analytics

## Overview
An enterprise-grade ELT (Extract, Load, Transform) pipeline designed for B2B restaurant equipment sales. This project extracts synthetic order data, loads it into a cloud data warehouse, and transforms it into highly optimized datasets for Business Intelligence (BI) reporting. The entire workflow is containerized and orchestrated for daily automated execution.

## Tech Stack
* **Orchestration & Containerization:** Apache Airflow, Docker
* **Data Warehouse:** Snowflake
* **Data Transformation (ELT):** SQL (Snowsight Views)
* **Extraction & Loading:** Python 3 (`snowflake-connector-python`, `Faker`)

## Pipeline Architecture
1. **Extract:** A Python script generates randomized B2B kitchen equipment orders (e.g., Convection Ovens, Dough Mixers) matching a restaurant supply catalog.
2. **Load:** The raw JSON data is bulk-inserted directly into a Snowflake `RAW_DATA` schema.
3. **Transform:** Snowflake SQL scripts transform the raw data into a dimensional Star Schema, creating reusable views (`reporting_product_performance`) that calculate total revenue, units sold, and average order value per product.
4. **Orchestrate:** Apache Airflow manages task dependencies and scheduling, running locally via a custom Docker container (SequentialExecutor).

## Setup Instructions
1. Clone the repository and configure a `.env` file with `SNOWFLAKE_USER`, `SNOWFLAKE_PASSWORD`, and `SNOWFLAKE_ACCOUNT`.
2. Run `docker-compose up -d` to build the Airflow environment.
3. Access the Airflow UI at `http://localhost:8080` (admin/admin).
4. Unpause and trigger the `hendi_b2b_pipeline` DAG.
