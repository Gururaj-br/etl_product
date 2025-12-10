import pandas as pd

from engine.base import Engine
from config import *

class PandasEngine(Engine):
    def __init__(self, conn):
        super().__init__(conn)

    def run(self):
        print("Running Pandas Engine")
        customers = pd.read_sql("SELECT * FROM customers", self.conn.connection)
        orders = pd.read_sql("SELECT * FROM orders", self.conn.connection)
        order_items = pd.read_sql("SELECT * FROM order_items", self.conn.connection)

        filtered_customers = customers[(customers['age'] >= 18) & (customers['age'] <= 35)]
        merged = filtered_customers.merge(orders, on='customer_id').merge(order_items, on='order_id')
        grouped = merged.groupby(['customer_id', 'age', 'item']).agg({'quantity': 'sum'}).reset_index()
        grouped = grouped.rename(columns={'quantity': 'total_quantity'})
        filtered = grouped[grouped['total_quantity'] > 0]
        return filtered.to_dict('records')