import mysql.connector
myconn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sms@1325",
  database="sanikadb"
)

#print(myconn)

mycursor = myconn.cursor()

#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
 # print(x)

#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

#mycursor.execute("SHOW TABLES")

#for x in mycursor:
 # print(x)

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val =  [
  ('Sanika', 'Paris 12'),
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)


myconn.commit()

print(mycursor.rowcount, "record inserted.")

myresult = mycursor.fetchall()
for x in myresult:
  print(x)
