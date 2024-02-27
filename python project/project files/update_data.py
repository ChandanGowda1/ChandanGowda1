# updating the new password where email or phone and old password matches

import mysql.connector, random


search_item = input('Enter  account_number or phone: ')
print('''TO update
password press 1
email press 2
phone number 3''')
search = int(input('Enter number to update:'))

try:
    conn = mysql.connector.connect(host = 'localhost', user = 'root',
                        password = '@RootPassword12', database = 'Banking')

    #print(conn.is_connected())

    cur = conn.cursor()
    
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
        old_email = input('Enter your old email: ')
        import smtplib,random
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login('forpythonc@gmail.com','kbvx mmgl vizt aell')
        
        
        otp = random.randint(1000,9999)
                    
        
        message = f"subject:{'otp'}\n\n Your otp to update email is {otp}"
        s.sendmail("forpythonc@gmail.com",old_email,message)
            
        s.quit()
        n_otp = int(input('enter otp sent to your mail: '))

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
            print('Invalid otp')
            conn.commit()

    elif  search ==3:
        import pywhatkit,random
        old_phone = int(input('Enter your old phone number:'))
        r = random.randint(1000,9999)
        msg = f'your otp to change phone number is {r}'        
        pywhatkit.sendwhatmsg(f'+91{old_phone}',msg,18,47 )

        new_phone = int(input('Enter your new phone number:'))
        sql = f'''update Netbanking set phone_number = '{new_phone}'
                where (account_number = '{search_item}' or phone_number = '{search_item}') and old_phone = '{old_phone}'
                '''
        
        cur.execute(sql)

        row_count = cur.rowcount

        if row_count > 0:
            print('phone number Changed')
        else:
            print('phone number Not Changed')

        conn.commit()

except mysql.connector.Error as err:
    print(err)

finally:
    conn.close()

