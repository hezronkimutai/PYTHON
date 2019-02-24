'''import the flask framework'''
from flask import Flask

'''give the app a name'''
app = Flask(__name__)

'''define your endpoint using the route decorator'''
@app.route('/')
def hello():
    return "hello world"

@app.route('/hello')
def first():
    c = "6+7"
    return c

'''Check if the name is equal to main'''
if __name__ == "__main__":
    '''Run he app'''
    app.run()
