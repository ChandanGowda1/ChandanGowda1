#importing modules
import mysql.connector,random,pywhatkit,smtplib

conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '@RootPassword12',
        database = 'Banking')
          
cur = conn.cursor()


#account overview
def view_data():
 try:    

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

 except mysql.connector.Error as ex:
    print(ex)
 



# updating the new password where email or phone and old password matches



def update_data():
 search_item = input('Enter  account_number or phone: ')
 print('''TO update
 password press 1
 email press 2
 phone number 3''')
 search = int(input('Enter number to update:'))
 try: 
    if search == 1:
        old_pwd = input('Enter your old password: ')
        new_pwd = input('Enter your new password: ')

        sql = f'''update Netbanking set password = '{new_pwd}'
                where (account_number = '{search_item}' or phone_number = '{search_item}') and password = '{old_pwd}'
            '''
    
        cur.execute(sql)

        row_count = cur.rowcount

        if row_count > 0:
            print('Password Changed')
        else:
            print('Password Not Changed')

        conn.commit()
    elif  search == 2:
        import random
        old_email = input('Enter your old email: ')        
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login('forpythonc@gmail.com','kbvx mmgl vizt aell')
                
        otp = random.randint(1000,9999)
        
        message = f"subject:{'Bank'}\n\n Your otp to update email is {otp}"
        s.sendmail("forpythonc@gmail.com",old_email,message)
            
        s.quit()
        n_otp = int(input('Enter otp sent to your email: '))        

        if  n_otp == otp:  
        
            new_email = input('Enter your new email: ')

            sql = f'''update Netbanking set email = '{new_email}'
                    where (account_number = '{search_item}' or phone_number = '{search_item}') and email = '{old_email}'
                '''
        
            cur.execute(sql)

            row_count = cur.rowcount

            if row_count > 0:
                print('email Changed')
            else:            
                print('email Not Changed')
        else:
            print('Invalid opt! ')

            conn.commit()

    elif  search ==3:
        import pywhatkit,random
        old_phone = int(input('Enter your old phone number:'))
        r = random.randint(1000,9999)
        msg = f'your otp to change phone number is {r}'        
        pywhatkit.sendwhatmsg_instantly(f'+91{old_phone}',msg,47 )

        otp = int(input('Enter otp sent to your number:'))
        if otp == r:            
            new_phone = int(input('Enter your new phone number:'))
            sql = f'''update Netbanking set phone_number = '{new_phone}'
                    where (account_number = '{search_item}' or phone_number = '{search_item}') and old_phone = '{old_phone}'
                    '''
            
            cur.execute(sql)

            row_count = cur.rowcount

            if row_count > 0:
                print('Phone number Changed')
            else:
                print('phone number Not!')

            conn.commit()
        else:
            print('Invalid otp!')

 except mysql.connector.Error as err:
    print(err)

 

#balance check
def balance_check(): 

 search = input('Enter your password:')
 try:
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




#apply new atm card
def atm_card():

 pwd = input('Enter your password:')
 msg = int(input('''TO apply for new ATM card you need to block old ATM card ,
                TO block press1 or to cancle press 0: '''))
 if msg == 1:
    try:        
        cur.execute('Select * from netbanking')
        datas = cur.fetchall()
        row = cur.rowcount
        for data in datas:
            if pwd in data:                    
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
                        msg = ''' Your request for new ATM card is accepted,
                        it will be deleverd within 15days if not requested by you then please visit bank immediately!'''
                        s = smtplib.SMTP('smtp.gmail.com',587)
                        s.starttls()
                        s.login('forpythonc@gmail.com','kbvx mmgl vizt aell')
                        message = f"subject:{'Bank'}\n\n {msg}"
                        s.sendmail("forpythonc@gmail.com",data[9],message)
                        break
                        
                    else:
                        print('please try again!')
                    conn.commit
                else:
                    print(' OTP is Incorrect!')
            elif pwd not in data:
                print('Invalid password!')
       
        
    except mysql.connector.Error as er:
        print(er)


#send money
def send_money(): 
 try: 
    sndr = input('Enter senders number:')
    if len(sndr) == 10:
        amnt = int(input('Enter amount to send:'))
        pwd = input('Enter your password:')
        cur = conn.cursor()
        cur.execute('select * from netbanking')
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

 except mysql.connector.Error as ex:
    print(ex)
 


#def checkbook

def checkbook(): 
 search = input('Enter your password or account_number:')

 try:
    cur.execute('Select * from netbanking')
    datas = cur.fetchall()
    for data in datas:
        if search in data:
            msg = 'checkBook Requested!'
            cur.execute(f'''update Netbanking set check_book = '{msg}' ''')                
            row_count = cur.rowcount
    
            if row_count > 0:
                print('Issue of CheckBook Requestd!')
                msg = ''' Your request for new checkBook is accepted,
                        it will be deleverd within 15days if not requested by you then please visit bank immediately!'''
                s = smtplib.SMTP('smtp.gmail.com',587)
                s.starttls()
                s.login('forpythonc@gmail.com','kbvx mmgl vizt aell')
                message = f"subject:{'Bank'}\n\n {msg}"
                s.sendmail("forpythonc@gmail.com",data[9],message)        
                break
        else:
            print('account not fetched!')                    
    conn.commit()               
               
 except mysql.connector.Error as ex:
    print(ex)

 
 
 




#main calling function
pwd = input('Enter your password:')
try :
    
    cur.execute('Select * from Netbanking')
    data = cur.fetchall()
    row = cur.rowcount

    if row > 0:
        for line in data:
            if pwd in line:
                end = 'go'
                while end == 'go' and end != 'stop':                    
                    search = int(input('''
                    press 1 for account overview,
                    press 2 for upadate details,
                    press 3 for Balance check,
                    press 4 for send money,
                    press 5 for apply New Atmcard,
                    press 6 for apply New checkbook,
                    Enter the  number:'''))
                    
                    if search == 1:
                        view_data()     
                    elif search == 2:
                        update_data()
                    elif search == 3:
                        balance_check()
                    elif search == 4:
                        send_money()
                    elif search == 5:
                        atm_card()
                    elif search == 6:
                        checkbook()
                    else:
                        print('choose correct option!')
                    end = input('Enter stop to quit or Enter go to move further:')
                        
           

    else:
        print('data not found!')
    

except ModuleNotFoundError as er:
    print(er)
conn.close()





