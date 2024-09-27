import pymysql
import os

import pymysql.cursors

class Database:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            cursorclass=pymysql.cursors.DictCursor
        )

    def query(self, query, *args):
        with self.connection.cursor() as cursor:
            cursor.execute(query, args=args)
            resultado = cursor.fetchall()
        self.connection.commit()

        return resultado
    
db = Database(
    host=os.environ.get('DB_HOST'),
    port=int(os.environ.get('DB_PORT')),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSWORD'),
    database=os.environ.get('DB_DATABASE'),
)
