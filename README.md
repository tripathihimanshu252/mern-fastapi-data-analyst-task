# Technical Assignment - Data Analyst & Fullstack Developer
**Candidate Name:** Himanshu Tripathi  
**Branch:** AI AND DS (GNIOT)  

## Project Overview
This project is an end-to-end data pipeline that cleans raw CSV data, performs business analysis, and serves the results through a FastAPI backend to a React-based dashboard[cite: 1].

## Features
- **Data Cleaning:** Automated Python script to handle duplicates, fix date formats, and impute missing values using Pandas[cite: 1].
- **Analysis:** Merges multiple datasets to calculate monthly revenue and top 10 customers[cite: 1].
- **REST API:** FastAPI endpoints to serve processed data in JSON format[cite: 1].
- **Dashboard:** Responsive React application with interactive Recharts visualizations[cite: 1].

## How to Run the Project

### Prerequisites
- Python 3.9+
- Node.js & npm

### Step 1: Data Processing
Run the following commands from the root folder:
```bash
pip install pandas
python scripts/clean_data.py
python scripts/analyze.py