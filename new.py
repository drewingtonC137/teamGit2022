import mysql.connector

print("go")

mydb = mysql.connector.connect(
    host ="localhost",
    user="root",
    password="",
    database="q13"
)

myCursor = mydb.cursor()

myCursor.execute("SELECT * FROM boot")

boten = myCursor.fetchall()

for boot in boten:
    print(boot[1])

bootnaam = input("Hoe heet je niuewe boot?")
sql = "INSERT INTO boot (kapitein, naam) VALUES (%s, %s)"
val = ('robinson', bootnaam)
myCursor.execute(sql, val)
mydb.commit()
