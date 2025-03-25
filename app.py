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

@app.route('/db_insert')
def insert():
    conn = psycopg2.connect("postgresql://postgresql_lab10_zj3u_user:fxTXSGOWrx9udgkmfKkmKv58JSQbtMl2@dpg-cvgu7ftumphs73cvu9eg-a/postgresql_lab10_zj3u")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30)
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15)
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()

    return "Basketball Table Successfully Populated"


@app.route('/db_select')
def select():
    conn = psycopg2.connect('postgresql://postgresql_lab10_zj3u_user:fxTXSGOWrx9udgkmfKkmKv58JSQbtMl2@dpg-cvgu7ftumphs73cvu9eg-a/postgresql_lab10_zj3u')
    cur = conn.cursor()
    cur.exectue('''
        SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close()
    response_string=""
    response_string += "<table>"
    for player in records:
        response_string += "<tr>"
        for info in player:
            response_string += "<td>{}</td>".format(info)
        response_string += "</tr>"
    response_string += "</table>"
    return response_string

@app.route('/db_drop')
def drop():
    conn = psycopg2.connect('postgresql://postgresql_lab10_zj3u_user:fxTXSGOWrx9udgkmfKkmKv58JSQbtMl2@dpg-cvgu7ftumphs73cvu9eg-a/postgresql_lab10_zj3u')
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;    
    ''')
    conn.commit()
    conn.close()
    return "Basketball table dropped successfully"