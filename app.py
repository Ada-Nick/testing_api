from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/hello/')
def hello_world():
    return 'Hello World!\n'

@app.route('/hello/<Samara>') # dynamic route
def hello_user(Samara):
    return 'Why Hello %s!\n' % Samara

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug= True)