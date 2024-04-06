import sqlite3
connection=sqlite3.connect("ashif.db")
cursor=connection.cursor()
sql_command="""
CREATE TABLE karthi(
rollno INTEGER,
name VARCHAR(20)
);"""
cursor.execute(sql_command)
sql_command="""
INSERT INTO karthi (rollno,name) VALUES (1,'prithiv'); """
cursor.execute(sql_command)
connection.commit()
connection.close()
print("Database created successfully")
