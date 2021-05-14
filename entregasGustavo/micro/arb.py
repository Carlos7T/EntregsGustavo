from flask import Blueprint,jsonify,request
from cnx.db_sepo import DataBase

arbCp=Blueprint('busquedaCP',__name__)
arbEstado=Blueprint('busquedaEstado',__name__)
arbColonia=Blueprint('busquedaColonia',__name__)

@arbCp.route('/busquedaCP',methods=['POST','GET'])
def cp():
	cx=DataBase()

	if request.method=='POST':
		cp=request.form['cpPrin']
		print(cp)
		sql="SELECT CONCAT('[',GROUP_CONCAT(JSON_OBJECT('lugar',d_asenta,'tipo',d_tipo_asenta,'municipio',D_mnpio,'estado',d_estado,'cp',d_codigo)),']') as res FROM sepo.codigo_postal_mexico where d_codigo='"+cp+"';"
	else:
		sql="SELECT CONCAT('[',GROUP_CONCAT(JSON_OBJECT('lugar',d_asenta,'tipo',d_tipo_asenta,'municipio',D_mnpio,'estado',d_estado,'cp',d_codigo)),']') as res FROM sepo.codigo_postal_mexico;"	

	cursor=cx.ejecutar(sql)

	results=cursor.fetchall()

	#print (sql)
	for row in results:
	   json = row[0]
	   

	return json

@arbEstado.route('/busquedaEstado',methods=['POST','GET'])
def estado():
	cx=DataBase()

	if request.method=='POST':
		estado=request.form['cpPrin']
		print(estado)
		sql="SELECT CONCAT('[',GROUP_CONCAT(JSON_OBJECT('lugar',d_asenta,'tipo',d_tipo_asenta,'municipio',D_mnpio,'estado',d_estado,'cp',d_codigo)),']') as res FROM sepo.codigo_postal_mexico where d_estado='"+estado+"';"
	else:
		sql="SELECT CONCAT('[',GROUP_CONCAT(JSON_OBJECT('lugar',d_asenta,'tipo',d_tipo_asenta,'municipio',D_mnpio,'estado',d_estado,'cp',d_codigo)),']') as res FROM sepo.codigo_postal_mexico;"	

	cursor=cx.ejecutar(sql)

	results=cursor.fetchall()

	#print (sql)
	for row in results:
	   json = row[0]
	   

	return json

@arbColonia.route('/busquedaColonia',methods=['POST','GET'])
def colonia():
	cx=DataBase()

	if request.method=='POST':
		colonia=request.form['cpPrin']
		print(colonia)
		sql="SELECT CONCAT('[',GROUP_CONCAT(JSON_OBJECT('lugar',d_asenta,'tipo',d_tipo_asenta,'municipio',D_mnpio,'estado',d_estado,'cp',d_codigo)),']') as res FROM sepo.codigo_postal_mexico where d_asenta='"+colonia+"';"
	else:
		sql="SELECT CONCAT('[',GROUP_CONCAT(JSON_OBJECT('lugar',d_asenta,'tipo',d_tipo_asenta,'municipio',D_mnpio,'estado',d_estado,'cp',d_codigo)),']') as res FROM sepo.codigo_postal_mexico;"	

	cursor=cx.ejecutar(sql)
	results=cursor.fetchall()
	for row in results:
	   json = row[0]
	   

	return json

