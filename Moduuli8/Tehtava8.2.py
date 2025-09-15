import mysql.connector

yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='123456789',
        autocommit=True
        )

maakoodi = input("Anna maakoodi: ")

sql = f'select count(type), type from airport where iso_country=\"{maakoodi}\" group by type';

kursori = yhteys.cursor()
kursori.execute(sql)

tulos = kursori.fetchall()

print(tulosmaakoodi)
