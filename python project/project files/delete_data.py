# delete record where email or phone and password matches

import mysql.connector, random

# accepting input from user
search_item = input('Enter account number or phone: ')


try:
    conn = mysql.connector.connect(host = 'localhost', user = 'root',
                        password = '@RootPassword12', database = 'Banking')

    print(conn.is_connected())

    cur = conn.cursor()

    sql = f'''delete from netbankig
            where (account_number = '{search_item}' or phone_number = '{search_item}')'''
    
    cur.execute(sql)

    row_count = cur.rowcount

    if row_count > 0:
        print('Record Deleted')
    else:
        print('Record Not Deleted')

    conn.commit()    

except mysql.connector.Error as err:
    print(err)

finally:
    conn.close()

