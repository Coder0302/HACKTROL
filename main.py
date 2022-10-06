from flask import Flask, request
import os

print("Hallo")
app = Flask(__name__)

action = ''

@app.route("/")
def hello():
    global action
    result = ''
    if request.args['msg'] != 'check':
        result = action
    else:
        action += request.args['msg']
    return result

ON_HEROKU = os.environ.get('ON_HEROKU')

if ON_HEROKU:
    # get the heroku port
    portt = int(os.environ.get('PORT', 17995))  # as per OP comments default is 17995
else:
    portt = 3000
print(portt)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=portt)

print("Bye")
