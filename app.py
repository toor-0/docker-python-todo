from flask import Flask, request, jsonify
import psycopg2
import time

app = Flask(__name__)

def get_connection():
    while True:
        try:
            conn = psycopg2.connect(
                host="db",
                database="tasksdb",
                user="postgres",
                password="password"
            )
            return conn
        except:
            print("Waiting for database...")
            time.sleep(2)

@app.route('/')
def home():
    return "Todo API with DB is running"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT task FROM tasks;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    tasks = [row[0] for row in rows]
    return jsonify(tasks)

@app.route('/add', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get("task")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (task) VALUES (%s);", (task,))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Task added"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
