import pymysql.cursors

from engine.base import Engine
from config import *

class SqlEngine(Engine):
    def __init__(self, conn):
        super().__init__(conn)
        self.age = (18, 35)  # Example age range filter

    def run(self):
        print("Running SQL Engine")
        query = f"""
        SELECT c.customer_id, c.age, oi.item, SUM(oi.quantity) as total_quantity
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        JOIN order_items oi ON o.order_id = oi.order_id
        WHERE c.age BETWEEN {self.age[0]} AND {self.age[1]}
        GROUP BY c.customer_id, c.age, oi.item
        HAVING SUM(oi.quantity) > 0
        """
        with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
        return results