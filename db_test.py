import psycopg2


DB_CONFIG = {
    "host": "xx.xx.xx.xx",
    "port": 5432,
    "database": "postgres",
    "user": "postgres",
    "password": "password"
}


def test_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)

        print("✅ Connected successfully!")

        cur = conn.cursor()

        cur.execute("SELECT version();")

        version = cur.fetchone()

        print("\nPostgreSQL Version:")
        print(version[0])

        cur.close()
        conn.close()

        print("\n✅ Connection closed.")

    except Exception as e:
        print(f"\n❌ Connection failed: {e}")


if __name__ == "__main__":
    test_connection()