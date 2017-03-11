from flask import request
from flask import Flask
app = Flask(__name__)

@app.route('/log')
def login():
    username = request.args.get('un')
    return un
   # password = request.args.get('pw')

if __name__ == '__main__':
    app.run()
