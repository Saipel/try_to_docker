import os
import psycopg2
#import json

DB_NAME = os.getenv("POSTGRES_DB", "default_db")
DB_USER = os.getenv("POSTGRES_USER", "default_user")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "default_password")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")

def get_db_donnect():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

def give_dict_conn_data():
    return dict(
        DB_NAME = os.getenv("POSTGRES_DB", "default_db"),
        DB_USER = os.getenv("POSTGRES_USER", "default_user"),
        DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "default_password"),
        DB_HOST = os.getenv("POSTGRES_HOST", "localhost"),
        DB_PORT = os.getenv("POSTGRES_PORT", "5432")
    )
