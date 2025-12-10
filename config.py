class DB_Config:
    DB_HOST = "localhost"
    DB_USER = "etl_user"
    DB_PASSWORD = ""
    DB_NAME = "etl_test"
    DB_PORT = 3306

class Report_Config:
    HEADERS = {
        "customer_id": "Customer",
        "age": "Age",
        "item_name": "Item",
        "total_quantity": "Quantity",
    }

    REPORT_FOLDER_PATH = "reports/"
    REPORT_FILE_NAME = "etl_{}_report_{}.csv"