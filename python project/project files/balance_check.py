
import mysql.connector

search = input('Enter your password:')
try:
    conn = mysql.connector.connect(host = 'localhost', user = 'root',
                                   password = '@RootPassword12', database = 'Banking')
    cur = conn.cursor()

    sql = 'select * from netbanking '
    cur.execute(sql)
    data = cur.fetchall()
    row = cur.rowcount

    if row > 0:
        for line in data:
            if search in line:                    
                print(line[7])
                break
##            else:
##                print('data not found!')
##                break
    else:
        print('data not found!!')
except mysql.connector.Error as ex:
    print(ex)
conn.close()
