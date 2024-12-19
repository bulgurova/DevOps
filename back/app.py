from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

# Подключение к базе данных SQL Server
def get_db_connection():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=db;DATABASE=master;UID=sa;PWD=YourStrong!Passw0rd')
    return conn

@app.route('/api', methods=['GET'])

def home():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/test', methods=['GET'])
def get_test_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM test')
    rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append({
            'id': row[0],
            'name': row[1]
        })
    cursor.close()
    conn.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
