from flask_cors import CORS
from flask import Flask
from flask import request

app = Flask(__name__)

CORS(app) #Prevents CORS errors 

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/get')
def get():
    state = request.args.get('state')
    with open('/home/pi/greenhouse/states/' + state + '.txt', 'r') as content_file:
        content = content_file.read()
    return content 

# A ne surtout pas faire !!!
@app.route('/call')
def call():
    call = request.args.get('call')
    switch = request.args.get('switch');
    with open('/home/pi/greenhouse/' + call + '_' + switch + '.py', 'r') as content_file:
        content = content_file.read()
    result =  exec(content)
    if switch=='ON' :
        return '1'
    else :
        return '0'
    
if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port = 8000)
