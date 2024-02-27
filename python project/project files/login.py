import mysql.connector
pwd = input('Enter your password:')
try :
    conn = mysql.connector.connect(host = 'localhost',
                                     user = 'root',
                                     password = '@RootPassword12',
                                     database = 'Banking')
    cur = conn.cursor()

    cur.execute('Select * from Netbanking')
    data = cur.fetchall()
    row = cur.rowcount

    if row > 0:
        for line in data:
            if pwd in line:
                end = 'go'
                while end != 'stop':
                        
                    search = int(input('''
                    press 1 for customer account overview,
                    press 2 for update customer details,
                    press 3 for delete customer,
                    press 4 for add new customer',
                    press 5 for search customer,
                    Enter the  number:'''))
                    if search == 1:
                        import viewdata.py
                    elif search == 2:
                        import update_data.py
                    elif search == 3:
                        import delete_data.py
                    elif search == 4:
                        import inserting_data.py                
                    elif search == 5:
                        import search_data.py
                    else:
                        print('choose correct option!')
                    end = input('Enter stop to quit or Enter go to move further:')
            else:
                print('Password is incorrect!')    

    else:
        print('data not found!')
    

except ModuleNotFoundError as er:
    print(er)
