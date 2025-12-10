import pandas as pd

from engine.base import Engine
from config import *

class PandasEngine(Engine):
    def __init__(self, conn):
        super().__init__(conn)
        self.min_age = 18
        self.max_age = 35

    def run(self):
        print("Running Pandas Engine")
        customer = pd.read_sql("SELECT * FROM customer", self.conn.connection)
        items = pd.read_sql("SELECT * FROM items", self.conn.connection)
        sales = pd.read_sql("SELECT * FROM sales", self.conn.connection)
        orders = pd.read_sql("SELECT * FROM orders", self.conn.connection)

        filtered_customers = customer[(customer['age'] >= self.min_age) & (customer['age'] <= self.max_age)]
        
        merged = filtered_customers.merge(sales, on='customer_id', how='left')
        merged = merged.merge(orders, on='sales_id', how='left')
        merged = merged.merge(items, on='item_id', how='left')
        
        merged['quantity'] = merged['quantity'].fillna(0).astype(int)
        
        grouped = merged.groupby(['customer_id', 'age', 'item_name']).agg({'quantity': 'sum'}).reset_index()
        grouped = grouped.rename(columns={'quantity': 'total_quantity'})
        
        filtered = grouped[grouped['total_quantity'] > 0]
        
        return filtered.to_dict('records')