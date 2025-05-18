import mysql.connector
from flask import g, Flask

app = Flask(__name__)

def get_db_connection():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host="localhost",
            user="nitsilchar",
            password="TAR0HA=#UMF_",
            database="lipsync"
        )
    return g.db

@app.teardown_appcontext
def close_db_connection(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def db_init():
    with app.app_context():
        connection = mysql.connector.connect(
            host="localhost",
            user="nitsilchar",
            password="TAR0HA=#UMF_"
        )
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS lipsync")
        cursor.close()
        connection.close()
        
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("USE lipsync")
        connection.commit()
        cursor.close()
