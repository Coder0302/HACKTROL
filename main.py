from flask import Flask
import os

print("Hallo")
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

ON_HEROKU = os.environ.get('ON_HEROKU')

if ON_HEROKU:
    # get the heroku port
    portt = int(os.environ.get('PORT', 17995))  # as per OP comments default is 17995
else:
    portt = 3000
print(portt)

if __name__ == "__main__":
    app.run(host='hacktrol.herokuapp.com', port=portt)

print("Bye")
