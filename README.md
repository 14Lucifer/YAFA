# Flask PostgreSQL Connection Tester

This Flask application provides a simple web interface to test PostgreSQL database connection. It allows users to input PostgreSQL database connection parameters and check whether the connection can be established successfully.

## Prerequisites

- Python 3.x
- Flask
- psycopg2

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/your_repository.git
    ```

2. Install dependencies:

    ```bash
    pip install Flask psycopg2
    ```

## Usage

1. Navigate to the project directory.

2. Run the Flask application:

    ```bash
    python app.py
    ```

3. Open a web browser and go to [http://localhost:80](http://localhost:80).

4. Enter PostgreSQL database connection details:
    - Hostname
    - Port
    - Database name
    - Username
    - Password

5. Click the "Test Connection" button.

6. The application will display the connection status.

## Files

- `app.py`: Contains the Flask application code.
- `index.html`: Homepage template for the web interface.
- `postgres.html`: Template for the PostgreSQL connection page.