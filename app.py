from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Mitch A in 3308!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://postgresql_lab10_zj3u_user:fxTXSGOWrx9udgkmfKkmKv58JSQbtMl2@dpg-cvgu7ftumphs73cvu9eg-a/postgresql_lab10_zj3u")
    conn.close()
    return "Database connection successful"


@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgresql://postgresql_lab10_zj3u_user:fxTXSGOWrx9udgkmfKkmKv58JSQbtMl2@dpg-cvgu7ftumphs73cvu9eg-a/postgresql_lab10_zj3u")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int   
            );
    ''')
    conn.commit()
    conn.close()
    return "Basketball table created successfully"