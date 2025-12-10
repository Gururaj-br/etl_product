# ETL Pipeline

ETL system that aggregates customer purchase data by item and exports to CSV.

## Quick Start

### 1. Database Setup
```bash
mysql -u etl_user -p etl_test < schema.sql
mysql -u etl_user -p etl_test < sample_data.sql
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Update config.py
Edit `config.py` with your MySQL credentials:
```
DB_HOST = "localhost"
DB_USER = "etl_user"
DB_PASSWORD = ""  # your password
DB_NAME = "etl_test"
```

### 4. Run
```bash
# SQL engine (default)
python main.py

# Pandas engine
python main.py pandas
```

## Output
CSV file saved to `reports/etl_<Engine Type>report_YYYYMMDD_HHMMSS.csv`

Format: `Customer;Age;Item;Quantity`

## How It Works
- Filters customers aged 18-35
- Groups purchases by customer and item
- Sums quantities across multiple purchases
- Excludes zero-quantity items
- Supports both SQL and Pandas processing
- Added new sql table called Pipeline to keep track of status of process run

