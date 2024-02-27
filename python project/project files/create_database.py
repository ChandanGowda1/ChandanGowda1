import mysql.connector
try:
    conn = mysql.connector.connect(host = 'localhost',
                                   user = 'root',
                                   password = '@RootPassword12',
                                   database = 'stud')
    print('Connection Established!')
    cur = conn.cursor()



    q = '''create table if not exists Internetbanking(Id int primary key auto_increment ,
            Password varchar(20) not null, 
            First_Name varchar(20) not null,
            last_Name varchar(20) not null,
            phone_number bigint(10) not null unique,
            account_number bigint(20)not null unique,
            Balance decimal(10,2),
            Email varchar(50) not null unique)'''
    cur.execute(q)

    print('Table created')

    conn.commit()
    
except mysql.connector.Error as ex:
    print(ex)

def view_data():
    from prettytable import PrettyTable
    pt = PrettyTable()

    q = "desc Internetbanking"

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
view_data()
conn.close()






