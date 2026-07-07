import psycopg2


DB_CONFIG = {
    "host": "xx.xx.xx.xx",
    "port": 5432,
    "database": "postgres",
    "user": "postgres",
    "password": "password"
}


def test_query():
    conn = psycopg2.connect(**DB_CONFIG)

    cur = conn.cursor()

    cur.execute("""
        SELECT tables
        FROM information_schema.tables
        WHERE table_schema = 'public'
    """)

    tables = cur.fetchall()

    print("\nTables:")

    for table in tables:
        print(table[0])

    cur.close()
    conn.close()


if __name__ == "__main__":
    test_query()