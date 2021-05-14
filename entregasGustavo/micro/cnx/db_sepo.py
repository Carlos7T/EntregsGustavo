import pymysql

class DataBase:
	def __init__(self):
		self.db=pymysql.connect(
			host='localhost',user='root',
			password='',db='sepo'
		)
		self.cursor=self.db.cursor()

	def ejecutar(self,sql):
		self.cursor.execute(sql)

		return self.cursor

	def closeDB(self):
		self.db.close()
		print("Base de datos desconectada")

	def comit(self):
		self.db.commit()
		return
	
	def rollback(self):
		self.db.rollback()	
		return