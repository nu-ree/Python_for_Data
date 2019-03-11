# $ mkdir flask-vue-crud
# $ cd flask-vue-crud
# $ python3 -m venv tutorial-env 
# $ tutorial-env\Scripts\activate.bat #for Window -- https://docs.python.org/ko/3/tutorial/venv.html
# $ source tutorial-env/bin/activate # for Ubuntu
# pip install Flask==1.0.2 Flask-Cors==3.0.4

from flask import Flask, jsonify
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()