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
                end = 'move'
                while  end == 'go' end != 'stop':
                    search = int(input('''
                    press 1 for account overview,
                    press 2 for upadate details,
                    press 3 for Balance check,
                    press 4 for send money',
                    press 5 for apply New Atmcard,
                    press 6 for apply New checkbook,
                    Enter the  number:'''))
                    
                    if search == 1:
                        import account_overview
                    elif search == 2:
                        import update_data
                    elif search == 3:
                        import balance_check
                    elif search == 4:
                        import send_money
                    elif search == 5:
                        import atm_card
                    elif search == 6:
                        import checkbook
                    else:
                        print('choose correct option!')
                    end = input('Enter stop to quit or Enter go to move further:')
                        
            else:
                print('Password is incorrect!')    

    else:
        print('data not found!')
    

except ModuleNotFoundError as er:
    print(er)






