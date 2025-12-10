import sys

from config import *
from db import DBConnection
from pipeline import Pipeline
from engine.sql_engine import SqlEngine
from engine.pandas_engine import PandasEngine
from reports.writer import ReportWriter

def main():
    try:
        DB_HOST = DB_Config.DB_HOST
        DB_USER = DB_Config.DB_USER
        DB_PASSWORD = DB_Config.DB_PASSWORD
        DB_NAME = DB_Config.DB_NAME
        DB_PORT = DB_Config.DB_PORT

        db_conn = DBConnection(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT)
    except Exception as e:
        print(f"Database db_connection error: {e}")
        sys.exit(1)
        
    pipeline = Pipeline("customer_etl", db_conn)
    pipeline.start()

    engine_type = sys.argv[1] if len(sys.argv) > 1 else "sql"
    if engine_type == "pandas":
        engine = PandasEngine(db_conn)
    else:
        engine = SqlEngine(db_conn)

    try:
        try:
            pipeline.process_start("extract_transform")
            data = engine.run()
            pipeline.process_success("extract_transform")
        except Exception as e:
            pipeline.process_fail("extract_transform")
            raise e

        try:    
            pipeline.process_start("load")
            rep_obj = ReportWriter(data)
            rep_obj.write_report()
            pipeline.process_success("load")
        except Exception as e:
            pipeline.process_fail("load")
            raise e
        
    except Exception as e:
        pipeline.process_fail("extract_transform")
        pipeline.process_fail("load")
        raise
    finally:
        pipeline.close()
        db_conn.close()

if __name__ == "__main__":
    main()