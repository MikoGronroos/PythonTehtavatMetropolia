from geopy import distance
import mysql.connector

icao01 = input("Anna 1 icao: ")
icao02 = input("Anna 2 icao: ")

yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='123456789',
        autocommit=True
        )

kursori = yhteys.cursor()

def haeAsiat(icao):
    sql = f'select latitude_deg, longitude_deg from airport where airport.ident = \"{icao}\"';
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return (tulos[0])

print(f'{distance.distance(haeAsiat(icao01), haeAsiat(icao02)).km} km')
