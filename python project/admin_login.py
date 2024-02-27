import mysql.connector

conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '@RootPassword12',
        database = 'Banking')

    
cur = conn.cursor()


#view data

def view_data():
 import mysql.connector
 try:
    
    from prettytable import PrettyTable
    pt = PrettyTable()
    
    q = 'select * from netbanking'
    cur.execute(q)
    data = cur.fetchall()
    pt.filed_names = cur.column_names
    row = cur.rowcount

    if row>0:
        for line in data:
            pt.add_row(line)
        print(pt) 
    else:
        print('Data not found')
 except mysql.connector.Error as ex:
    print(ex)

    



#update data
def update_data():
 search_item = input('Enter  account_number or phone: ')
 print('''FOR update
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
        old_email = input('Enter your old email: ')
        import smtplib,random
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login('forpythonc@gmail.com','kbvx mmgl vizt aell')
        
        def gen():
            otp = random.randint(1000,9999)
            return otp            
        
        message = f"subject:{'otp'}\n\n Your otp to update email is {gen()}"
        s.sendmail("forpythonc@gmail.com",old_email,message)
            
        s.quit()
        n_otp = int(input('enter otp sent to your mail'))

        if  n_opt == gen():  
        
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

            conn.commit()
     

    elif  search ==3:
        import pywhatkit,random
        old_phone = int(input('Enter your old phone number:'))
        r = random.randint(1000,9999)
        msg = f'your otp to change phone number is {r}'        
        pywhatkit.sendwhatmsg_instantly(f'+91{old_phone}',msg,30)
        otp = int(input('Enter otp sent to your whatsapp:'))

        if r == otp:
            
            new_phone = int(input('Enter your new phone number:'))
            sql = f'''update Netbanking set phone_number = '{new_phone}'
                    where (account_number = '{search_item}' or phone_number = '{search_item}') and phone_number = '{old_phone}'
                    '''
            
            cur.execute(sql)

            row_count = cur.rowcount

            if row_count > 0:
                print('phone number Changed')
            else:
                print('phone number Not Changed')
        else:
            print('invalid opt')
        conn.commit()
 except mysql.connector.Error as err:
    print(err)

 


# delete record where email or phone and password matches

import mysql.connector, random
def delete_data():

 search_item = input('Enter customer account number or customer password to delete: ')
 

 try:

    sql = f'''delete from netbanking 
            where (account_number = '{search_item}' or password = '{search_item}')'''
    
    cur.execute(sql)

    row_count = cur.rowcount

    if row_count > 0:
        print('Record Deleted')
    else:
        print('Record Not Deleted')

    conn.commit()    

 except mysql.connector.Error as err:
    print(err)

 


#inserting data
def inserting_data():

 import mysql.connector , random

 fn = input('Customer First_name:')
 ln = input('Customer Last_name:')
 while True:    
    gen = input('Enter Customer gender(m/f):')
    if gen in ('m','f'):
        break
 ph = int(input('Enter Customer phone number:'))
 em = input('Enter Customer  email:')
 bal = int(input('Enter Customer account balance:'))
 pwd = input('Create password for customer:')
 acc = random.randint(1000000000,99999999999)
 try:
 
    sql = f'''insert into 
            Netbanking(first_name,last_name,gender,password,phone_number,email,balance,account_number)
            values('{fn}','{ln}','{gen}','{pwd}','{ph}','{em}','{bal}','{acc}')'''
    
    cur.execute(sql)
    
    row_count = cur.rowcount

    if row_count>0:
        print('Record inserted')

    conn.commit()
 except mysql.connector.Error as ex:
    print(ex)

 
        

#search data  
def search_data():

 import mysql.connector
 try:   
    from prettytable import PrettyTable
    pt = PrettyTable()

    search_item = input('Enter account_number/phone to search: ')
    
    q = f"select * from netbanking where account_number = '{search_item}' or phone_number = '{search_item}'"

    cur.execute(q)
    
    data = cur.fetchall()
    
    pt.field_names = cur.column_names

    row = cur.rowcount

    if row > 0:
        # print(data)
        for line in data:
            pt.add_row(line)

        print(pt)
        
    else:
        print('No Records Found')
            
 except mysql.connector.errors.Error as ex:
    print(ex)

 


    

#Main calling function
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
                press 1 for customers accounts overview,
                press 2 for update customer details,
                press 3 for delete customer,
                press 4 for add new customer,
                press 5 for search customer,
                Enter the  number:'''))
                if search == 1:
                    view_data()
                elif search == 2:
                    update_data()
                elif search == 3:
                    delete_data()
                elif search == 4:
                    inserting_data()
                elif search == 5:
                    search_data()
                end = input('TO move further enter go and to quit press stop:')
            else:
                print('Account not fetched!')    

    else:
        print('data not found!')
    

except ModuleNotFoundError as er:
    print(er)
finally :
    conn.close()
