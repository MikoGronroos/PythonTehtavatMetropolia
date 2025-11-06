from flask import Flask, request, jsonify

app = Flask(__name__)



@app.route('/alkuluku', methods=['GET'])
def alkuluku():
    args = request.args
    luku = int(args.get("luku1"))
    onAlkuluku = True
    for x in range(luku):
        numero = x + 1
        if float(luku) % numero == 0 and (numero != 1 and numero != luku):
            onAlkuluku = False
            break
    values = {"Number": f"{str(luku)}", "isPrime": f"{str(onAlkuluku)}"}
    return jsonify(values)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
