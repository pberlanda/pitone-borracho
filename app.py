from flask import Flask, jsonify, request

app = Flask(__name__)

# dati finti (usiamo file di testo in formato JSON senza usare db)
libri = [
    {"id":1, "titolo": "L'uomo invisibile"},
    {"id":2, "titolo": "1984"},
    {"id":3, "titolo": "La metamorfosi"},
    {"id":4, "titolo": "Io sono leggenda"},
    {"id":5, "titolo": "Moby Dick"}
]

# GET → recupera tutti i libri
@app.route("/libri", methods=["GET"])
def get_libri():
    return jsonify(libri)

# GET → recupera un libro per id
@app.route("/libri/<int:id>", methods=["GET"])
def get_libro(id):
    # TEST return("Bingo!")
    for libro in libri:
        if id==libro["id"]:
            # TEST return "Super bingo!"
            return jsonify(libro)
        
    return jsonify("not found"), 404

# POST → aggiungi un nuovo libro
@app.route("/libri", methods=["POST"])
def add_libro():
    nuovo = request.get_json
    libri.append(nuovo)
    return jsonify(nuovo), 201 # 201 risorsa creata su server

# impedisco che il programma venga avviato da un altro file
if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000, debug=True) # in codespaces devi secificare host con questo IP