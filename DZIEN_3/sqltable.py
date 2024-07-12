import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',port=3306,database='baza_nowedane')
cursorObject = db.cursor()

tabela_student = """
CREATE TABLE IF NOT EXISTS student(
firstname varchar(100),
lastname varchar(100),
nrstudenta int primary key
);
"""

cursorObject.execute(tabela_student)

dodaj_st = "INSERT INTO student(firstname,lastname,nrstudenta) values(%s,%s,%s);"
val_one = ("Jan","Kot",756547)
cursorObject.execute(dodaj_st,val_one)

val_multi = [
("Janusz","Knot",545343),
("Janina","Szczot",7567567),
("Olga","Nowak",212343),
("Piotr","Kos",98445),
("Nadia","Ros",23222),
("Olaf","Polak",23255),
]
cursorObject.executemany(dodaj_st,val_multi)

db.commit()
db.close()
