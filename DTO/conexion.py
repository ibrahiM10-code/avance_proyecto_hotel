import pymysql

class Conexion:
    def __init__(self,database, db_host, db_password, db_user):
        self.db = pymysql.connect(db=database, host=db_host, user=db_user, password=db_password)
        self.cursor = self.db.cursor()

    def ejecutar_query(self, sql_query):
        self.cursor.execute(sql_query)
        return self.cursor
    
    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()

    def disconnect(self):
        self.db.close()
