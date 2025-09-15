import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='123456789',
         autocommit=True
         )

sql = 'select * from goal'

kursori = yhteys.cursor()
kursori.execute(sql)

tulos = kursori.fetchall()

if kursori.rowcount > 0:
    for rivi in tulos:
        print(rivi[1])
