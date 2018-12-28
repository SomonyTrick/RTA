import sqlite3

def init():
    conn = sqlite3.connect('rta.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE Position
        (ID Integer PRIMARY KEY [autoincrement] NOT NULL,
        Projectname TEXT    NOT NULL,
        Company INT     NOT NULL,
        Post CHAR(50),
        Persons CHAR(50),
        Edu CHAR(50),
        Degree CHAR(50),
        Majors CHAR(50),
        Target CHAR(50),
        Status CHAR(50));''')
    conn.commit()
    conn.close()

def save(position):
    conn = sqlite3.connect('rta.db')

    cursor = conn.cursor()
    cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
    cursor.close()
    
    conn.commit()
    conn.close()