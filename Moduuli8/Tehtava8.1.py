import mysql.connector

yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='123456789',
        autocommit=True
        )

icao = input("Anna icao: ")

sql = f'select name from airport where airport.ident = \"{icao}\"'
kursori = yhteys.cursor()
kursori.execute(sql);

tulos = kursori.fetchall()

print(tulos[0])
