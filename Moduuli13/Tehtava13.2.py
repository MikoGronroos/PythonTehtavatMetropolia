from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)



@app.route('/kentta', methods=['GET'])
def kentta():
    args = request.args
    icao = str(args.get("icao"))
    yhteys = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',
            user='root',
            password='123456789',
            autocommit=True
            )

    sql = f'select name, municipality from airport where airport.ident = \"{icao}\"'
    kursori = yhteys.cursor()
    kursori.execute(sql);

    tulos = kursori.fetchall()
    values = {"ICAO": f"{icao}", "Name": f"{tulos[0][0]}", "Municipality": f"{tulos[0][1]}"}
    return jsonify(values)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
