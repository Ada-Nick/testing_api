from flask import Flask
app = Flask(__name__)

@app.route('/')
def base():
    return 0
@app.route('/hello/')
def hello_world():
    return 'Hello World!\n'

@app.route('/hello/<username>') # dynamic route
def hello_user(username):
    
    return 'Why Hello %s!\n' % username

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug= True)