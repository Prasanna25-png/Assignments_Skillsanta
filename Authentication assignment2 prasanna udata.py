
database={'Prasanna25':

{'Name':'Prasanna',

'Age':20,

'Email':'udataprasanna1213@gamil.com',

'Password':'pra2501',

'Balance':20000},

'Abhishek11':{'Name':'Abhishek',

'Age':21,

'Email':'abhinyak6271@gamil.com',

'Password':'abhi1101',

'Balance':35000}}

while True:

  print('1. Sign in\n','2. Sign up\n','3. Log out\n')

  c=int(input())

  if c==1:

      user=str(input('Enter Username: '))

      password=str(input('Enter Password: '))

      if user in database.keys():

        if password==database[user]['Password']:

          print(f"Login Successful\nWelcome{database[user]['Name']}")

      

         

          while True:

            print('\nEnter your choice: \n1. Check Balance\n2. Deposit Balance\n3.           Withdrawal\n4. Log out')

            choice=int(input())

            if choice==1:

              print(database[user]['Balance'])

            elif choice==2:

              amt=int(input('Enter Ammount: '))

              database[user]['Balance']+=amt

            elif choice== 3:

              cash=int(input('Enter Ammount: '))

              database[user]['Balance']-=cash

            elif choice==4:

              break

        else:

           print('Password Failed')

          

      else:

           print('Account is not exist')

  elif c==2:
 
        a=input("Enter Username: ")
        v=str(input("Enter your name: "))
        w=int(input("Enter your age: "))
        x=str(input("Enter your email: "))
        y=str(input("Enter your password: "))
        z=int(input("Enter your balance: "))
        database.update({a:{'name':v,'Age':w,'Email':x,'Password':y,'Balance':z}})
        print('Account created successfuly')

  elif c==3:

      break

