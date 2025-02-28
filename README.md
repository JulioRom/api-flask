# To-Do API | Flask Python 3

Este proyecto es una API REST desarrollada con **Flask** para gestionar una lista de tareas (*to-dos*). La API permite realizar las siguientes operaciones:

## 📌 Funcionalidades
- `GET /todos` - Obtiene la lista de tareas.
- `POST /todos` - Agrega una nueva tarea.
- `DELETE /todos/<int:position>` - Elimina una tarea por su posición en la lista.

## 📁 Estructura del Proyecto
```
flask_todo_api/
│── venv/            # Entorno virtual
│── app.py           # Código principal de la API
│── requirements.txt # Dependencias del proyecto
```

## 🚀 Instalación y Configuración
### 1️⃣ Crear un Entorno Virtual
```bash
python -m venv venv  # Crear el entorno virtual
```
- En Windows:
  ```bash
  venv\Scripts\activate
  ```
- En macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 2️⃣ Instalar Dependencias
```bash
pip install Flask
```
Para confirmar la instalación:
```bash
python -m flask --version
```

### 3️⃣ Ejecutar la API
```bash
python app.py
```
La API se ejecutará en `http://127.0.0.1:5000/`

---
📌 **Con esto, tienes una API funcional en Flask para manejar tareas! 🚀**

