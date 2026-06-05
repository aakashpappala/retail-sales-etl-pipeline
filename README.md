# Retail Sales ETL Pipeline

## Overview

This project demonstrates an ETL (Extract, Transform, Load) pipeline built using Python, Pandas, PostgreSQL, and SQL. The pipeline processes retail sales data, performs data cleaning and transformation, and loads the processed data into PostgreSQL for reporting and analysis.

## Technologies Used

* Python
* Pandas
* PostgreSQL
* SQL
* SQLAlchemy
* Git & GitHub

## Project Workflow

### Extract

* Read retail sales data from CSV files using Pandas.

### Transform

* Cleaned and validated sales data.
* Performed data transformation and revenue calculations.
* Improved data quality through validation checks.

### Load

* Loaded transformed data into PostgreSQL using SQLAlchemy.
* Stored processed records for reporting and analysis.

## Project Structure

retail-sales-etl-pipeline/

├── data/

│   ├── sales_data.csv

│   └── cleaned_sales.csv

├── scripts/

│   ├── extract.py

│   ├── transform.py

│   ├── load.py

│   └── main.py

├── sql/

│   ├── schema.sql

│   └── queries.sql

├── requirements.txt

├── .gitignore

└── README.md

## Sample SQL Reports

### Total Revenue

SELECT SUM(total_amount) AS total_revenue
FROM sales;

### Product-wise Revenue Analysis

SELECT product,
SUM(total_amount) AS total_revenue
FROM sales
GROUP BY product;

## Key Features

* ETL Pipeline Development
* Data Cleaning and Transformation
* PostgreSQL Integration
* SQL Reporting and Analysis
* Workflow Automation using Python

## Future Enhancements

* Azure Data Factory Integration
* Cloud Storage Integration
* Automated Scheduling using Apache Airflow
* Dashboard Creation using Power BI
