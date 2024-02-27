import mysql.connector
try:
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '@RootPassword12',
        database = 'Banking')

    print('Connection established')
    cur = conn.cursor()


    
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

conn.close()
