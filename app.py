from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aquahobby.db'

db = SQLAlchemy(app)

class Aquarium(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(60), nullable=False)
   volume = db.Column(db.Integer, nullable=False)
   temperature = db.Column(db.Float, nullable=False)
   ph = db.Column(db.Float, nullable=False)

@app.route('/api/aquarium/add', methods=["POST"])
def create_aquarium():
  data = request.json

  required_fields = ["name", "volume", "temperature", "ph"]
  if not all(field in data for field in required_fields):
    return jsonify({"message": "Dados inválidos: campos obrigatórios ausentes"}), 400

  if not isinstance(data["name"], str):
    return jsonify({"message": "O nome deve ser uma string"}), 400
    
  if not isinstance(data["volume"], int):
    return jsonify({"message": "O volume deve ser um número inteiro"}), 400

  if not isinstance(data["temperature"], (int, float)):
    return jsonify({"message": "A temperatura deve ser um número"}), 400

  if not isinstance(data["ph"], (int, float)):
    return jsonify({"message": "O pH deve ser um número"}), 400
  
  aquarium = Aquarium(name=data["name"], volume=data["volume"], temperature=data["temperature"], ph=data["ph"])
  db.session.add(aquarium)
  db.session.commit()
  return jsonify({"message": "Aquário criado com sucesso!"})

@app.route('/api/aquarium/delete/<int:aquarium_id>', methods=["DELETE"])
def delete_aquarium(aquarium_id):
  aquarium = Aquarium.query.get(aquarium_id)
  if aquarium:
    db.session.delete(aquarium)
    db.session.commit()
    return jsonify({"message": "Aquário removido com sucesso!"})
  return jsonify({"message": "Aquário não encontrado!"}), 404

@app.route('/api/aquarium/<int:aquarium_id>', methods=["GET"])
def get_aquarium_details(aquarium_id):
  aquarium = Aquarium.query.get(aquarium_id)
  if aquarium:
    return jsonify({
      "id": aquarium.id,
      "nome": aquarium.name,
      "volume": aquarium.volume,
      "temperatura": aquarium.temperature,
      "ph": aquarium.ph
    })
  return jsonify({"message": "Aquário não encontrado!"}), 404

@app.route('/api/aquarium/update/<int:aquarium_id>', methods=["PUT"])
def update_aquarium(aquarium_id):
  aquarium = Aquarium.query.get(aquarium_id)
  if not aquarium:
    return jsonify({"message": "Aquário não encontrado!"}), 404
  
  data = request.json
  if 'name' in data:
    if not isinstance(data["name"], str):
      return jsonify({"message": "O nome deve ser uma string"}), 400
    aquarium.name = data['name']

  if 'volume' in data:
    if not isinstance(data["volume"], int):
      return jsonify({"message": "O volume deve ser um número inteiro"}), 400
    aquarium.volume = data['volume']

  if 'temperature' in data:  
    if not isinstance(data["temperature"], (int, float)):
      return jsonify({"message": "A temperatura deve ser um número"}), 400
    aquarium.temperature = data['temperature']

  if 'ph' in data:
    if not isinstance(data["ph"], (int, float)):
      return jsonify({"message": "O pH deve ser um número"}), 400
    aquarium.ph = data['ph']
  db.session.commit()
  return jsonify({"message": "Aquário atualizado com sucesso!"})

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == "__main__":
  app.run(debug=True)