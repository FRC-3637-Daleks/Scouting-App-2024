from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'Scouting'

TABLES = {}
TABLES['Auton'] = (
    "CREATE TABLE `Auton` ("
    "   `Team` int NOT NULL,"
    "   `Match_Number` int NOT NULL,"
    "   `Color` VARCHAR(1),"
    "   `High_Cube` int,"
    "   `High_Cone` int,"
    "   `Mid_Cube` int,"
    "   `Mid_Cone` int,"
    "   `Low_Cube` int,"
    "   `Low_Cone` int,"
    "   `Left_Platform` VARCHAR(1),"
    "   `Out_of_Community` VARCHAR(1),"
    "   PRIMARY KEY (`Team`, `Match_Number`)"
    ")"
)

TABLES['Teleop'] = (
    "CREATE TABLE `Teleop` ("
    "   `Team` int NOT NULL,"
    "   `Match_Number` int NOT NULL,"
    "   `Color` VARCHAR(1),"
    "   `Moved` VARCHAR(1),"
    "   `High_Cube` int,"
    "   `High_Cone` int,"
    "   `Mid_Cube` int,"
    "   `Mid_Cone` int,"
    "   `Low_Cube` int,"
    "   `Low_Cone` int,"
    "   PRIMARY KEY (`Team`, `Match_Number`)"
    ")"
)

TABLES['Defense'] = (
    "CREATE TABLE `Defense` ("
    "   `Team` int NOT NULL,"
    "   `Match_Number` int NOT NULL,"
    "   `Color` VARCHAR(1),"
    "   `Blocked_Others` VARCHAR(1),"
    "   PRIMARY KEY (`Team`, `Match_Number`)"
    ")"
)

TABLES['Endgame'] = (
    "CREATE TABLE `Endgame` ("
    "   `Team` int NOT NULL,"
    "   `Match_Number` int NOT NULL,"
    "   `Color` VARCHAR(1),"
    "   `Charge_Status` VARCHAR(1),"
    "   `Win` VARCHAR(1),"
    "   PRIMARY KEY (`Team`, `Match_Number`)"
    ")"
)

#todo: set max char of mediumtext in the index script

TABLES['Comments'] = (
    "CREATE TABLE `Comments` ("
    "   `Team` int NOT NULL,"
    "   `Match_Number` int NOT NULL,"
    "   `Color` VARCHAR(1),"
    "   `Insert_Comments` MEDIUMTEXT,"
    "   PRIMARY KEY (`Team`, `Match_Number`)"
    ")"
)

TABLES['Pit'] = (
    "CREATE TABLE `Pit`("
    "   `Team` int NOT NULL,"
    "   `Match_Number` int NOT NULL DEFAULT 0,"    # Sets defualt match number to 0
    "   `Length` int,"
    "   `Width` int,"
    "   `Weight` int,"
    "   `Intake` MEDIUMTEXT,"
    "   `Scoring` MEDIUMTEXT,"
    "   `Drivebase` MEDIUMTEXT,"
    "   `Auton` MEDIUMTEXT,"
    "   `Defense` VARCHAR(1),"
    "   `Start_Position` VARCHAR(1),"
    "   `Preferred_Substation` VARCHAR(2),"
    "   `Triple_Balance` VARCHAR(1),"
    "   `Preferred_Piece` VARCHAR(4),"
    "   `Comments` MEDIUMTEXT,"
    "   `Photo` MEDIUMBLOB,"
    "   PRIMARY KEY (`Team`, `Match_Number`)"
    ")"
)

cnx = mysql.connector.connect(user="dalek", password="3637",
                        host="127.0.0.1",
                        database='Scouting')

cursor = cnx.cursor()

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("That table already exists!")
        else:
            print(err.msg)
    else:
        print("OK")
        

cursor.close()
cnx.close()