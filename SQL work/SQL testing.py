import sqlite3

def createTable():
    connector = sqlite3.connect("test.db")
    print("Opened database successfully")

    connector.execute('''CREATE TABLE COMPANY
    (staffID INT PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    room INT NOT NULL,
    address CHAR(50),
    salary REAL);''')

    print("Table created successfully")
    connector.close()

if __name__ == "__main__":
    createTable()