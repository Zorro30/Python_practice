import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datesatmp TEXT, keyword TEXT, value REAL)')

def data_entry():
    c.execute('INSERT INTO stuffToPlot VALUES(145123542, "3-12-2018", "Python", 5)')
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()