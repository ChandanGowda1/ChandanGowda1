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


def send_money():    
    sndr = input('Enter senders number:')
    if len(sndr) == 10:
        amnt = int(input('Enter amount to send:'))
        pwd = input('Enter your password:')        
        q = 'select * from netbanking'
        cur.execute(q)
        data = cur.fetchall()    
        row = cur.rowcount

        if row>0:
            for line in data:
                if pwd in line:                
                    bal= line[7]
                    if amnt < bal:
                        balance = bal - amnt                    
                        sql = f'''update Netbanking set Balance = '{balance}'
                                where  password = '{pwd}' '''
                        cur.execute(sql)
                        row = cur.rowcount                    
                        if row>0:
                           print('Amount sent sucessfully!')                        
                        conn.commit()
                    else :
                        print('You dont have sufficent amount to send!')
                    
                    break
                print('Incorrect password!')
        else:
            print('Data not found')
    else:
       print('Invalid number , please check the number!')
send_money()


conn.close()
