from flask import Flask, request
import os

print("Hallo")
app = Flask(__name__)

isKillGame = False
action = '0'

@app.route("/")
def hello():
    global action, isKillGame
    result = ''
    if !isKillGame:
        if request.args['device'] == 'comp':
            if request.args['action'] == 'check':
                result = action
                action = '0'
        elif request.args['device'] == 'phone':
            if request.args['action'] == 'send':
                action = request.args['doaction']
            if request.args['action'] == 'kill':
                result = '1'
                isKillGame = True
        return result
    else 
        return 1

ON_HEROKU = os.environ.get('ON_HEROKU')

if ON_HEROKU:
    # get the heroku port
    portt = int(os.environ.get('PORT', 17995))  # as per OP comments default is 17995
else:
    portt = 3000
print(portt)

if __name__ == "__main__":
    app.run(port=portt)

print("Bye")
