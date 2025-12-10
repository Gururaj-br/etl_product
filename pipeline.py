import uuid
import hashlib
from datetime import datetime

class Pipeline:
    def __init__(self, process_name, conn):
        self.process_name = process_name
        self.conn = conn
        self.job_token = None

    def start(self):
        self.job_token = hashlib.sha256(uuid.uuid4().hex.encode()).hexdigest()[:64]
        print(f"Pipeline started | process={self.process_name} | token={self.job_token}")

    def process_start(self, step_name):
        with self.conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO pipeline_run (job_token, process_name, step_name, status, start_time)
                VALUES (%s, %s, %s, 'RUNNING', %s)
            """, (self.job_token, self.process_name, step_name, datetime.now()))
        self.conn.commit()

    def process_success(self, step_name):
        with self.conn.cursor() as cursor:
            cursor.execute("""
                UPDATE pipeline_run SET status = 'SUCCESS', end_time = %s
                WHERE job_token = %s AND step_name = %s
            """, (datetime.now(), self.job_token, step_name))
        self.conn.commit()

    def process_fail(self, step_name):
        with self.conn.cursor() as cursor:
            cursor.execute("""
                UPDATE pipeline_run SET status = 'FAILED', end_time = %s
                WHERE job_token = %s AND step_name = %s
            """, (datetime.now(), self.job_token, step_name))
        self.conn.commit()

    def close(self):
        pass