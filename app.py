from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId  # Añade esta línea para importar ObjectId
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])

# Conecta a la base de datos MongoDB
client = MongoClient('mongodb+srv://rmrivera:freeforever2021@learningcluster.5ye61vd.mongodb.net/')
db = client['administrador']
calificaciones = db["califications"]

# Obtener todas las calificaciones
@app.route('/califications', methods=['GET'])
def obtener_calificaciones():
    resultados = []
    for calificacion in calificaciones.find():
        resultados.append({
            '_id': str(calificacion['_id']),
            'Unit': calificacion['Unit'],
            'Name': calificacion['Name'],
            'Description': calificacion['Description'],
            'Grade': calificacion['Grade']
        })
    return jsonify(resultados)

# Crear una nueva calificación
@app.route('/califications', methods=['POST'])
def crear_calificacion():
    nueva_calificacion = {
        'Unit': request.json['Unit'],
        'Name': request.json['Name'],
        'Description': request.json['Description'],
        'Grade': request.json['Grade']
    }
    resultado = calificaciones.insert_one(nueva_calificacion)
    return jsonify({'mensaje': 'Calificación creada con éxito', 'id': str(resultado.inserted_id)})

# Eliminar las calificaciones definidas
@app.route('/califications/<id>', methods=['DELETE'])
def eliminar_calificacion(id):
    resultado = calificaciones.delete_one({'_id': ObjectId(id)})
    if resultado.deleted_count == 1:
        return jsonify({'mensaje': 'Calificación eliminada con éxito'})
    else:
        return jsonify({'mensaje': 'Calificación no encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)

