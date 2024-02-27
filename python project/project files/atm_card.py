import mysql.connector
import random
import pywhatkit
import smtplib

pwd = input('Enter your password:')
msg = int(input('''TO apply for new ATM card you need to block old ATM card ,
                TO block press1 or to cancle press 0: '''))
if msg == 1:
    try:
        conn = mysql.connector.connect (host = 'localhost',
                                        user = 'root',
                                        password = '@RootPassword12',
                                        database = 'Banking')
        cur = conn.cursor()
        cur.execute('Select * from netbanking')
        datas = cur.fetchall()
        row = cur.rowcount
        for data in datas:
            if pwd in data:
                print(f'+91{data[5]}')
        
                r = random.randint(1000,9999)                
                msg = f'Hi your otp to block atm card is {r}'                
                pywhatkit.sendwhatmsg_instantly(f'+91{data[5]}',msg,30 )                                
                pwd = int(input('Enter OTP sent to ur Regestred whatsapp number:'))

                if pwd == r:
                    print('Your Old ATM card is blocked! ')
                    msg = 'REQUESTED NEW ATMCARD !'
                    cur.execute(f'''update netbanking set ATM_card = '{msg}' ''')
                    rw = cur.rowcount
                    
                    if rw > 0:
                        print('Your New ATM card Requsted!')
##                        message = '''subject:{'BANK'}\n\n Your request for new ATM card is accepted,
##                        it will be deleverd within 15days if not requested by you
##                        then please visit bank immediately!'''
##                        s = smtplib.SMTP('smtp.gmail.com',587)
##                        s.starttls()
##                        s.login('forpythonc@gmail.com','kbvx mmgl vizt aell')
##                        s.sendmail('forpythonc@gmail.com',f'{data[10]}',message)
                    else:
                        print('please try again!')
                    conn.commit
                else:
                    print(' OTP is Incorrect!')
            else:
                print('Invalid password!')
        conn.close()        
        
    except mysql.connector.Error as er:
        print(er)


    


               

    
    
