from flask import Flask
from routes.route import app as route_app

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(route_app)

if __name__ == '__main__':
    app.run(debug=True)