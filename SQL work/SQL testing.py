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


def insertData():
    connector = sqlite3.connect("test.db")
    connector.execute("INSERT INTO COMPANY (staffID,name,room,address,salary)"
                      "VALUES (1, 'Paul', 32, 'STOKE', 20000.00)");

    connector.execute("INSERT INTO COMPANY (staffID,name,room,address,salary)"
                      "VALUES (123, 'Kurt', 44, 'STOKE', 20000.00)");

    connector.commit()
    print("Records created successfully")
    connector.close()


if __name__ == "__main__":
    createTable()
    insertData()

#  Use SQLITE3 viewer, view the database file, you should be able to see the records
