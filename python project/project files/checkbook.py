import mysql.connector
search = input('Enter your password or account_number:')
msg = 'checkBook Requested!'
try:
    conn = mysql.connector.connect(host = 'localhost',user = 'root',
                                   password = '@RootPassword12',database = 'Banking')
    cur = conn.cursor()

    sql = f'''update Netbanking set check_book = '{msg}'
                where (account_number = '{search}' or password = '{search}')
            '''
    
    cur.execute(sql)
    
    row = cur.rowcount
    
    if row > 0:
        print('Issue of CheckBook Requestd!')    
   
    else:
        print('account not fetched!')                    
    conn.commit()               
               
except mysql.connector.Error as ex:
    print(ex)

conn.close()
