import pymysql

class DBConnection:

    def __init__(self, host, user, password, db, port):
        self.connection = self.get_connection(host, user, password, db, port)
        if not self.connection:
            raise Exception("Failed to establish database connection.")
        
    def get_connection(self, host, user, password, db, port):
        try:
            return pymysql.connect(host=host, user=user, password=password, db=db, port=port)
        except pymysql.MySQLError as e:
            print(f"Error connecting to database: {e}")
            return None
    
    def close(self):
        if self.connection:
            self.connection.close()