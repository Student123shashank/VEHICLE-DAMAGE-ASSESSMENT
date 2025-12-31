import mysql.connector
import config

try:
    print("Attempting to connect to MySQL...")

    # Connect using credentials from config.py
    connection = mysql.connector.connect(**config.mysql_credentials)

    if connection.is_connected():
        print("✅ MySQL connection successful!")
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()[0]
        print("Connected to database:", db_name)

        # Optional: test if user_info table exists
        cursor.execute("SHOW TABLES;")
        tables = [t[0] for t in cursor.fetchall()]
        print("Tables found:", tables)

        if 'user_info' not in tables:
            print("⚠️ Table 'user_info' not found! You need to create it.")
        else:
            print("✅ Table 'user_info' exists!")

except mysql.connector.Error as e:
    print("❌ Error while connecting to MySQL:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed.")
