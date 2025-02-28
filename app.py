from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de tareas inicial
todos = [
    {"done": True, "label": "Sample Todo 1"},
    {"done": True, "label": "Sample Todo 2"}
]

# GET /todos - Retorna la lista de tareas
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# POST /todos - Agrega una nueva tarea
@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()  # Obtiene el JSON enviado en el request
    if not data or "label" not in data or "done" not in data:
        return jsonify({"error": "Invalid request"}), 400

    todos.append(data)  # Agrega la nueva tarea a la lista
    return jsonify(todos)

# DELETE /todos/<int:position> - Elimina una tarea en función de la posición
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Invalid position"}), 400

    todos.pop(position)  # Elimina la tarea de la lista
    return jsonify(todos)

# Ejecutar la aplicación solo si este archivo se ejecuta directamente
if __name__ == '__main__':
    app.run(debug=True)