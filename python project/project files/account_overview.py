import mysql.connector
try:
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '@RootPassword12',
        database = 'Banking')
          
    cur = conn.cursor()
except mysql.connector.Error as ex:
    print(ex)

def view_data():
    from prettytable import PrettyTable
    pt = PrettyTable()
    
    pwd = input('Enter your password:')
    q = 'select * from netbanking'
    cur.execute(q)
    data = cur.fetchall()
    pt.filed_names = cur.column_names
    row = cur.rowcount

    if row>0:
        for line in data:
            if pwd in line:
                pt.add_row(line)
                print(pt)
                break             
    else:
        print('Data not found')
view_data()     

conn.close()
