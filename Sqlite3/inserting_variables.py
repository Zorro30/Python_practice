import sqlite3
import datetime
import time
import random

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1234566, '3-12-2018', 'Python', 8)")
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp,keyword,value) VALUES(?, ?, ?, ?)",
            (unix, date,keyword,value))
    conn.commit()

# data_entry()
create_table()

for i in range(10):
    dynamic_data_entry()
    time.sleep(1)
c.close()
conn.close()
