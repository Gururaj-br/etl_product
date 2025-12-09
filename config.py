class DB_Config:
    DB_HOST = "localhost"
    DB_USER = "root"
    DB_PASSWORD = "root"
    DB_NAME = "etl_test"
    DB_PORT = 3306

class Report_Config:
    HEADERS = {
        "Customer": 1,
        "Age":1,
        "Item": 1,
        "Quantity": 1,
    }

    REPORT_FILE_PATH = "reports/"
    REPORT_FILE_NAME = "etl_report_{}.csv"

