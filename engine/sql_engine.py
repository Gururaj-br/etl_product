import pymysql.cursors

from engine.base import Engine
from config import *

class SqlEngine(Engine):
    def __init__(self, conn):
        super().__init__(conn)
        self.age_min = 18
        self.age_max = 35

    def run(self):
        print("Running SQL Engine")
        query = f"""
        SELECT c.customer_id, c.age, i.item_name, SUM(o.quantity) as total_quantity
        FROM customer c
        JOIN sales s ON c.customer_id = s.customer_id
        JOIN orders o ON s.sales_id = o.sales_id
        JOIN items i ON o.item_id = i.item_id
        WHERE c.age BETWEEN {self.age_min} AND {self.age_max}
        AND o.quantity IS NOT NULL
        GROUP BY c.customer_id, c.age, i.item_name
        HAVING SUM(o.quantity) > 0
        """
        with self.conn.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
        return results