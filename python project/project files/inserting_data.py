import mysql.connector , random

fn = input('first_name:')
ln = input('last_name:')
while True:    
    gen = input('enter gender(m/f):')
    if gen in ('m','f'):
        break
ph = int(input('Enter phone number:'))
em = input('Enter email:')
bal = int(input('Enter min balance:'))
pwd = input('Create password:')
acnt_nbr = random.randint(100000000,99999999999)

try:
    conn = mysql.connector.connect(host = 'localhost',
                                   user = 'root',
                                   password = '@RootPassword12',
                                   database = 'Banking')    
    cur = conn.cursor()
    sql = f'''insert into 
            Netbanking(first_name,last_name,gender,password,phone_number,email,balance,account_number)
            values('{fn}','{ln}','{gen}','{pwd}','{ph}','{em}','{bal}','{acnt_nbr}')'''
    
    cur.execute(sql)
    
    row_count = cur.rowcount

    if row_count>0:
        print('Record inserted')

    conn.commit()
except mysql.connector.Error as ex:
    print(ex)

conn.close()
        
    




    
