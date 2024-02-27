print('WELCOME TO BANK OF BANK')
print('*************************')


search = int(input('''press 1 for admin login:
press 2 for customer login:
press 3 to signup:
enter the number:'''))


if search == 1 :
    import admin_login
elif search == 2:
    import customer_login
    
elif search == 3:
   import inserting_data
   
else:
    print('Enter valid number!')
