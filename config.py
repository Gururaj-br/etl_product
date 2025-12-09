class DB_Config:
    DB_HOST = "localhost"
    DB_USER = "root"
    DB_PASSWORD = "root"
    DB_NAME = "etl_test"
    DB_PORT = 3306

class Report_Config:
    HEADERS = {
        "customer_name": "Customer",
        "age": "Age",
        "item": "Item",
        "quantity": "Quantity",
    }

    REPORT_FOLDER_PATH = "reports/"
    REPORT_FILE_NAME = "etl_report_{}.csv"

