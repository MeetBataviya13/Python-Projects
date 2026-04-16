import psycopg2

def connect_db():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="expense_manager",
            user="postgres",
            password="admin",
            port=5432
        )
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None


def close_db(connection):
    if connection:
        connection.close()