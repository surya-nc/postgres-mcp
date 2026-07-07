import os
from fastmcp import FastMCP
from db import get_connection

mcp = FastMCP("postgres-demo")


@mcp.tool
def get_tables() -> list[str]:
    """
    Returns all tables available in the public schema.
    """

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
        ORDER BY table_name
    """)

    tables = [row[0] for row in cur.fetchall()]

    cur.close()
    conn.close()

    return tables


@mcp.tool
def get_table_sample(
    table_name: str,
    limit: int = 10
) -> dict:
    """
    Returns sample rows from a table.

    Args:
        table_name: Name of the table.
        limit: Maximum number of rows to return.
    """

    conn = get_connection()
    cur = conn.cursor()

    # For demo purposes only.
    # Later we'll validate table names properly.
    cur.execute(
        f"SELECT * FROM {table_name} LIMIT %s",
        (limit,)
    )

    rows = cur.fetchall()

    columns = [desc[0] for desc in cur.description]

    cur.close()
    conn.close()

    return {
        "columns": columns,
        "rows": rows
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))

    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=port
    )