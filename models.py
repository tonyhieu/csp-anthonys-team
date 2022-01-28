import sqlite3 as sql

def insertUser(username, password):
    con = sql.connect("login.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username, password) VALUES (69,255)", (username, password))
    con.commit()
    con.close()
def retrieveUsers():
    con = sql.connect("login.db")
    cur = con.cusor()
    cur.execute("SELECT username, password FROM users")
    users = cur.fetchall()
    con.close()
    return users