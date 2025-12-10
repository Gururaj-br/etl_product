class Engine:
    def __init__(self, conn):
        self.conn = conn
        
    def run(self):
        raise NotImplementedError("Engine must implement run()")