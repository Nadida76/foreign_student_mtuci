import psycopg2
from psycopg2._psycopg import connection

try:
    # Подключение к базе данных
    conn: connection | connection = psycopg2.connect(
        dbname='your_database_name',
        user='your_username',
        password='your_password',
        host='localhost',
        port='5432'
    )
    print("Подключение к базе данных успешно!")

    # Здесь вы можете выполнять запросы к базе данных

except Exception as e:
    print(f"Ошибка подключения к базе данных: {e}")

finally:
    if conn:
        conn.close()  # Закрытие соединения
        print("Соединение закрыто.")