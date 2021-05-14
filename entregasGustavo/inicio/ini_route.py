from flask import Blueprint,render_template
import time

ini=Blueprint('ini', __name__,template_folder='templates',static_folder='static')

@ini.route('/ini')
def index():
	version=int(round(time.time() * 1000))
	return render_template('/index.html',version=version)




