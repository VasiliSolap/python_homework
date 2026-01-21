import sqlite3

def add_publisher(cursor, name):
    try:
        cursor.execute(
            "INSERT INTO publishers (name) VALUES (?)",
            (name,)
        )
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' already exists.")


def add_magazine(cursor, name, publisher_id):
    try:
        cursor.execute(
            "INSERT INTO magazines (name, publisher_id) VALUES (?, ?)",
            (name, publisher_id)
        )
    except sqlite3.IntegrityError as e:
        print(f"Could not add magazine '{name}': {e}")


def add_subscriber(cursor, name, address):
    cursor.execute(
        "SELECT subscriber_id FROM subscribers WHERE name = ? AND address = ?",
        (name, address)
    )
    if cursor.fetchone():
        print(f"Subscriber '{name}' at '{address}' already exists.")
        return

    cursor.execute(
        "INSERT INTO subscribers (name, address) VALUES (?, ?)",
        (name, address)
    )


def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
    cursor.execute(
        """
        SELECT subscription_id
        FROM subscriptions
        WHERE subscriber_id = ? AND magazine_id = ?
        """,
        (subscriber_id, magazine_id)
    )
    if cursor.fetchone():
        print("Subscription already exists.")
        return

    try:
        cursor.execute(
            """
            INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date)
            VALUES (?, ?, ?)
            """,
            (subscriber_id, magazine_id, expiration_date)
        )
    except sqlite3.IntegrityError as e:
        print(f"Could not add subscription: {e}")



try:
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        # create tables (как у тебя — без изменений)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS publishers (
                publisher_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS magazines (
                magazine_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                publisher_id INTEGER NOT NULL,
                FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscribers (
                subscriber_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                address TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                subscription_id INTEGER PRIMARY KEY,
                subscriber_id INTEGER NOT NULL,
                magazine_id INTEGER NOT NULL,
                expiration_date TEXT NOT NULL,
                FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id),
                FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id)
            )
        """)

       
        add_publisher(cursor, "Penguin")
        add_publisher(cursor, "O'Reilly")
        add_publisher(cursor, "Springer")

        add_magazine(cursor, "Python Weekly", 1)
        add_magazine(cursor, "Data Science Monthly", 2)
        add_magazine(cursor, "AI Today", 3)

        add_subscriber(cursor, "Alice", "123 Main St")
        add_subscriber(cursor, "Bob", "456 Oak Ave")
        add_subscriber(cursor, "Alice", "123 Main St")  # дубликат

        add_subscription(cursor, 1, 1, "2026-12-31")
        add_subscription(cursor, 2, 2, "2025-06-30")

        print("Tables populated successfully.")

        # 1. Retrieve all information from subscribers
        cursor.execute("SELECT * FROM subscribers")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        # 2. Retrieve all magazines sorted by name
        cursor.execute("SELECT * FROM magazines ORDER BY name")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        # 3. Find magazines for a particular publisher
        cursor.execute("""
            SELECT magazines.*
            FROM magazines
            JOIN publishers
            ON magazines.publisher_id = publishers.publisher_id
            WHERE publishers.name = ?
        """, ("Penguin",))

        rows = cursor.fetchall()

        for row in rows:
            print(row)

except sqlite3.Error as e:
    print("An error occurred:", e)


