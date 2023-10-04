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
                      "VALUES (1, 'Paul', 32, 'STOKE', 20000.00)")

    connector.execute("INSERT INTO COMPANY (staffID,name,room,address,salary)"
                      "VALUES (2, 'Kurt', 44, 'STOKE', 20000.00)")

    connector.commit()
    print("Records created successfully")
    connector.close()

def updateData():
    connector = sqlite3.connect("test.db")
    print("Opened database successfully")
    connector.execute("UPDATE COMPANY set SALARY = 25000.00 where staffID=2")
    # means update data in COMPANY table where ID = 2 the salary to 2500.00
    connector.commit()  # saves the changes
    print("Total number of rows updated :", connector.total_changes)
    # next lines print the records
    cursor = connector.execute("SELECT staffid, name, address, salary from COMPANY WHERE staffID == 2")
    # if you wanted to reference a string make sure to use another pair of apostrophes

    for row in cursor:
        print("staff ID == ", row[0])
        print("staff Name = ", row[1])
        print("staff ADDRESS = ", row[2])
        print("staff SALARY = ", row[3], "\n")
    print("operation done successfully")

    #  this function updates whoever is held in staff ID 2's salary to 25,000


def deleteRecord():
    connector = sqlite3.connect('test.db')
    print("Opened database successfully")

    # here we will delete record with ID = 2
    connector.execute("DELETE from COMPANY where staffID=2;")
    connector.commit()
    print("Total number of rows deleted :", connector.total_changes)

    # print records, record ID = 2 will disappeare.
    cursor = connector.execute("SELECT Staffid, name, address, salary from COMPANY  WHERE staffID == 2")

    # print records, record ID = 2 will disappeare.
    for row in cursor:
        print("staff ID == ", row[0])
        print("staff Name = ", row[1])
        print("staff ADDRESS = ", row[2])
        print("staff SALARY = ", row[3], "\n")
    print("operation done successfully")




if __name__ == "__main__":
    # createTable()
    # insertData()
    # updateData()
    deleteRecord()

#  Use SQLITE3 viewer, view the database file, you should be able to see the records
