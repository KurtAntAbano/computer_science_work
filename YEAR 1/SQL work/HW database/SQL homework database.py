import sqlite3
#  note: when writing SQL, python does not specifically tell you where errors are
# ? can be used to pass values (can also be done through variables)
# ? means save a space for what im about to put

def createTable():
    connector = sqlite3.connect("homework.db")
    print("Opened database successfully")

    connector.execute('''CREATE TABLE IF NOT EXISTS HOMEWORK_TBL
    (HOMEWORK  TEXT CHAR(15) PRIMARY KEY NOT NULL,
    SUBJECT TEXT CHAR(10) NOT NULL,
    DUE_DATE NOT NULL);''')

    print("Table created successfully")
    connector.close()


def insertData():
    givenHWK = input("enter your Homeworks name")
    givenSUB = input("enter the subject")
    givenDUE = input("enter the due date")

    connector = sqlite3.connect("homework.db")
    connector.execute("INSERT INTO HOMEWORK_TBL (HOMEWORK,SUBJECT,DUE_DATE)"
                      "VALUES (?,?,?)", (givenHWK,givenSUB,givenDUE))

    connector.commit()
    print("Records inserted successfully")
    connector.close()

def viewHomework():
    connector = sqlite3.connect("homework.db")

    cursor = connector.execute("SELECT HOMEWORK, SUBJECT, DUE_DATE from HOMEWORK_TBL")

    for row in cursor:
        print("Homework: ", row[0])
        print("subject: ", row[1])
        print("Due date: ", row[2], "\n")
    print("operation done successfully")


def searchHomework():
    target = input("Please input the due date of the homework u want")

    connector = sqlite3.connect("homework.db")

    homeworkList = connector.execute("SELECT HOMEWORK, SUBJECT, DUE_DATE from HOMEWORK_TBL")

    flag = False
    for row in homeworkList:
        for i in range(0, len(homeworkList)):
            if row[i] == target:
                print("found")
                flag = True
                homework = row[i - 2]
                print("your homework is", homework)
    if flag == False:
        print("not found")











if __name__ == "__main__":
    #createTable()
    #insertData()
    viewHomework()
    searchHomework()