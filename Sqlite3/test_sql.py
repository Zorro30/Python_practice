import sqlite3

conn = sqlite3.connect('parkingLot.db')
c = conn.cursor()
class regular(object):

    def create(self):
        c.execute('CREATE TABLE IF NOT EXISTS parkingTable(slot_no TEXT, reg_no TEXT, colour TEXT, total_time TEXT, charge TEXT)')

    def update(self):

        slot_no =4
        reg_no = 'MH'
        colour = 'white'
        c.execute("INSERT INTO parkingTable VALUES(:slot_no, :reg_no, :colour, :total_time, :charge)",
                {'slot_no':slot_no,'reg_no':reg_no,'colour':colour,'total_time':0,'charge':0})
        conn.commit()
        c.execute("SELECT * FROM parkingTable")
        # c.commit()
        data = c.fetchall()
        print(data) 

        conn.commit()
        c.close()
        conn.close()

call = regular()

call.create()
call.update()

