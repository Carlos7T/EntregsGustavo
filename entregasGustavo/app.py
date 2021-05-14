import flask
from inicio.ini_route import ini


app = flask.Flask(__name__)
app.register_blueprint(ini)
if __name__ == "__main__":
		app.run('0.0.0.0',9400,debug=True)


