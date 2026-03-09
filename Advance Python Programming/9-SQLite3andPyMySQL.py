#1.
# Write a Python program to create a database and a table using SQLite3.
import sqlite3

# Connect to SQLite database (it will create the file if it does not exist)
connection = sqlite3.connect("my_database.db")

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )
""")

print("Database and table created successfully!")

# Commit the changes and close the connection
connection.commit()
connection.close()

#2.
#Write a Python program to insert data into an SQLite3 database and fetch it.

import sqlite3

# Connect to SQLite database (will create the file if it doesn’t exist)
connection = sqlite3.connect("my_database.db")

# Create a cursor object
cursor = connection.cursor()

# Create table if it does not exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )
""")

# Insert data into table
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("sakshi", 20, "A"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("nisha", 22, "B"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("brijal", 21, "A"))

# Commit the changes
connection.commit()

print("Data inserted successfully!")

# Fetch all records
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("\nFetching data from students table:")
for row in rows:
    print(row)

# Close the connection
connection.close()
