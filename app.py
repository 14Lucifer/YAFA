from flask import Flask, request, render_template
import psycopg2
import socket
from psycopg2 import OperationalError

app = Flask(__name__)

@app.route('/')
def home():
    # Render the homepage template
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return render_template('index.html',hostname=hostname, ip_address=ip_address)

@app.route('/postgres', methods=['GET', 'POST'])
def postgre():
    message = ''
    if request.method == 'POST':
        hostname = request.form['hostname']
        port = request.form['port']
        dbname = request.form['dbname']
        user = request.form['user']
        password = request.form['password']
        message = test_postgres_connection(hostname, port, dbname, user, password)
    return render_template('postgres.html', message=message)

def test_postgres_connection(hostname, port, dbname, user, password):
    try:
        conn = psycopg2.connect(
            host=hostname,
            port=port,
            dbname=dbname,
            user=user,
            password=password
        )
        conn.close()
        return 'Connected successfully.'
    except OperationalError as e:
        return f'No connect: {e}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
