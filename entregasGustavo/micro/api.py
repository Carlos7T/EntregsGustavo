from flask import Flask,jsonify
from flask_cors import CORS
import arb



app = Flask(__name__)
CORS(app)
cors=CORS(app,resources={ r"/*":{ "origins":"*" }}) 


app.register_blueprint(arb.arbCp)
app.register_blueprint(arb.arbEstado)
app.register_blueprint(arb.arbColonia)
    
if __name__ == "__main__":
		app.run('0.0.0.0',9500,debug=True)