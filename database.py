import sqlite3
connection = sqlite3.connect('student.db')
cursor = connection.cursor()
create_table_query = """
CREATE TABLE IF NOT EXISTS student (
    NAME VARCHAR(25),
    COURSE VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
    );
    """
cursor.execute(create_table_query)
sql_query ="""Insert INTO student (NAME, COURSE, SECTION, MARKS) VALUES (?,?,?,?);"""
values =[
    ('Student1', 'Python', 'A', 90),
    ('Student2', 'Java', 'B', 85),
    ('Student3', 'C++', 'A', 95),
    ('Student4', 'JavaScript', 'C', 80),
    ('Student5', 'Python', 'B', 88)

]
cursor.executemany(sql_query, values)
connection.commit()
data = cursor.execute("""select * from student""")
for row in data:
    print(row)
if connection:
    connection.close()
    
