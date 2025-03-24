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
