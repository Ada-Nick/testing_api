from flask import Flask, render_template
import pymysql
app = Flask(__name__)


def create_database_connection():

    name = "admin"
    password = "finalpwd"
    db_name = "database1" 

    rds_host  = "database-1.c1oiit29cevl.eu-west-2.rds.amazonaws.com"

    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, port = 3306)

    return conn



@app.route('/')
def api():
    return render_template('api.html', loss= 0, pred = 0)
@app.route('/hello/')
def hello_world():
    return 'Hello World!\n'

@app.route('/hello/<username>') # dynamic route
def hello_user(username):
    
    return 'Why Hello %s!\n' % username

    

if __name__ == '__main__':
    app.run( debug= True)