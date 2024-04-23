import os
from flask import Flask, request, render_template
import psycopg2
import socket
from psycopg2 import OperationalError
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)


# Ensure the directory for log files exists
log_directory = "./log"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Set up logging to a file
log_file = os.path.join(log_directory, "app.log")
handler = RotatingFileHandler(log_file, maxBytes=10000, backupCount=3)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


@app.before_request
def log_request_info():
    # Attempt to get the user's real IP address if behind a proxy
    if 'X-Forwarded-For' in request.headers:
        ip_address = request.headers['X-Forwarded-For']  # If behind a proxy
    else:
        ip_address = request.remote_addr  # Direct IP address
    
    logger.info('Request received: IP %s, Method %s, URL %s', ip_address, request.method, request.url)

@app.after_request
def log_response_info(response):
    if 'X-Forwarded-For' in request.headers:
        ip_address = request.headers['X-Forwarded-For']
    else:
        ip_address = request.remote_addr
    
    logger.info('Response sent: IP %s, Method %s, URL %s, Status %s', ip_address, request.method, request.url, response.status)
    return response



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
