import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',port=3306,database='baza_nowedane')
cursorObject = db.cursor()

dane = 'SELECT firstname,lastname FROM student;'
cursorObject.execute(dane)

print(cursorObject)
wynik = cursorObject.fetchall()
print(type(wynik))

for x,y in wynik:
    print(f'imię: {x}, nazwisko: {y}')

print("_"*50)

dane = 'SELECT firstname,lastname FROM student WHERE nrstudenta>=70000;'
cursorObject.execute(dane)

print(cursorObject)
wynik = cursorObject.fetchall()
print(type(wynik))

print('wynik dla id>=70000\n')
for x,y in wynik:
    print(f'imię: {x}, nazwisko: {y}')

print("_"*50)

vquery = 'SELECT * FROM nv_stud;'
cursorObject.execute(vquery)
wv = cursorObject.fetchall()

for x in wv:
    print(f'student: {x}')

db.close()
