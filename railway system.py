import mysql.connector

def create_database_railway():
    mycon = mysql.connector.connect(host='localhost', user='root', passwd='qwertyuiop')
    cursor = mycon.cursor()
    mycon.autocommit = True
    s1 = "CREATE DATABASE railway"
    cursor.execute(s1)

create_database_railway()

def table_creation_railway():
    mycon = mysql.connector.connect(host='localhost', user='root', passwd='qwertyuiop', database='railway')
    cursor = mycon.cursor()
    mycon.autocommit = True
    s1 = '''CREATE TABLE railway(
                name VARCHAR(100),
                phno VARCHAR(15) PRIMARY KEY,
                age INT(4),
                gender VARCHAR(50),
                from_f VARCHAR(100),
                to_t VARCHAR(100),
                date_d VARCHAR(20)
            )'''
    cursor.execute(s1)

table_creation_railway()

def table_creation_user_accounts():
    mycon = mysql.connector.connect(host='localhost', user='root', passwd='qwertyuiop', database='railway')
    cursor = mycon.cursor()
    mycon.autocommit = True
    s1 = '''CREATE TABLE user_accounts(
                fname VARCHAR(100),
                lname VARCHAR(100),
                user_name VARCHAR(100),
                password VARCHAR(100) PRIMARY KEY,
                phno VARCHAR(15),
                gender VARCHAR(50),
                dob VARCHAR(50),
                age VARCHAR(4)
            )'''
    cursor.execute(s1)

table_creation_user_accounts()

def connection():
    mycon = mysql.connector.connect(host='localhost', user='root', passwd='qwertyuiop', database='railway')
    if mycon.is_connected():
        print("Successfully connected")

connection()

def menu():
    print('1. YES')
    print('2. NO')
    ch = int(input('DO YOU WANT TO CONTINUE OR NOT: '))
    
    while ch == 1:
        print('WELCOME TO ONLINE RAILWAY RESERVATION SYSTEM')
        print('1. SIGN IN')
        print('2. SIGN UP')
        print('3. DELETE ACCOUNT')
        print('4. EXIT')

        ch1 = int(input('ENTER YOUR CHOICE: '))

        if ch1 == 1:
            a = checking()
            if a:
                print('WELCOME')
                main()
            else:
                continue
        elif ch1 == 2:
            a = checking_1()
            if a:
                main()
            else:
                print('PASSWORD ALREADY EXISTS')
                continue
        elif ch1 == 3:
            c = checking_2()
            if c:
                print('ACCOUNT DELETED')
                continue
            else:
                print('YOUR PASSWORD OR USERNAME IS INCORRECT')
                continue
        elif ch1 == 4:
            print('THANK YOU')
            break
        else:
            print('ERROR 404: PAGE NOT FOUND')
            break

def main():
    print('1. YES')
    print('2. NO')
    c = int(input("DO YOU WANT TO CONTINUE OR NOT: "))

    while c == 1:
        print('1. TICKET BOOKING\n2. TICKET CHECKING\n3. TICKET CANCELLING\n4. ACCOUNT DETAILS\n5. LOG OUT')
        ch = int(input('ENTER YOUR CHOICE: '))

        if ch == 1:
            ticket_booking()
        elif ch == 2:
            ticket_checking()
        elif ch == 3:
            ticket_cancelling()
        elif ch == 4:
            checking_3()
        elif ch == 5:
            print('THANK YOU')
            break
        else:
            print('WRONG INPUT')
    else:
        print('ERROR 404: PAGE NOT FOUND')

def ticket_booking():
    mycon = mysql.connector.connect(host='localhost', user='root', passwd='qwertyuiop', database='railway')
    cursor = mycon.cursor()
    mycon.autocommit = True
    nm = input('ENTER YOUR NAME: ')
    phno = input('ENTER YOUR PHONE NUMBER: ')
    age = int(input('ENTER YOUR AGE: '))
    
    print('M = MALE\nF = FEMALE\nN = NOT TO MENTION')
    gender = input('ENTER YOUR GENDER: ').upper()
    
    fr = input('ENTER YOUR STARTING POINT: ')
    to = input('ENTER YOUR DESTINATION: ')
    date1 = input('ENTER DATE (DD): ')
    date2 = input('ENTER MONTH (MM): ')
    date3 = input('ENTER YEAR (YYYY): ')
    date = f"{date1}/{date2}/{date3}"
    
    gender_map = {'M': 'MALE', 'F': 'FEMALE', 'N': 'NOT TO MENTION'}
    v = gender_map.get(gender, 'NOT TO MENTION')
    
    s1 = f"INSERT INTO railway VALUES('{nm}', '{phno}', {age}, '{v}', '{fr}', '{to}', '{date}')"
    cursor.execute(s1)
    
    print('BOOKED SUCCESSFULLY')

def ticket_checking():
    mycon = mysql.connector.connect(host='localhost', user='root', passwd='qwertyuiop', database='railway')
    cursor = mycon.cursor()
    mycon.autocommit = True

    print('1. YES')
    print('2. NO')
    ch = int(input("DO YOU WANT TO CONTINUE OR NOT: "))

    if ch == 1:
        phno = input('ENTER YOUR PHONE NUMBER: ')
        try:
            s1 = f"SELECT * FROM railway WHERE phno='{phno}'"
            cursor.execute(s1)
            data = cursor.fetchone()
            
            if data:
                labels = ['NAME', 'PHONE NUMBER', 'AGE', 'GENDER', 'STARTING POINT', 'DESTINATION', 'DATE']
                for i, label in enumerate(labels):
                    print(f"{label} ::: {data[i].upper() if isinstance(data[i], str) else data[i]}")
            else:
                print('TICKET DOES NOT EXIST')
        except:
            print('ERROR OCCURRED')
    elif ch == 2:
        print('THANK YOU')
    else:
        print('ERROR 404: PAGE NOT FOUND')

def ticket_cancelling():
    mycon = mysql.connector.connect(host='localhost', user='root', passwd='qwertyuiop', database='railway')
    cursor = mycon.cursor()
    mycon.autocommit = True

    print('1. YES')
    print('2. NO')
    ch = int(input("DO YOU WANT TO CONTINUE OR NOT: "))
    
    if ch == 1:
        phno = input('ENTER YOUR PHONE NUMBER: ')
        s1 = f"DELETE FROM railway WHERE phno='{phno}'"
        cursor.execute(s1)
        print('TICKET CANCELLED')
    elif ch == 2:
        print('THANK YOU')
    else:
        print('ERROR 404: PAGE NOT FOUND')

def checking_2():
    mycon = mysql.connector.connect(host='localhost', user='root', passwd='qwertyuiop', database='railway')
    cursor = mycon.cursor()
    mycon.autocommit = True

    a = input('USER NAME: ')
    b = input('PASSWORD: ')
    
    try:
        s1 = f"SELECT user_name FROM user_accounts WHERE password='{b}'"
        cursor.execute(s1)
        data = cursor.fetchone()

        if data and data[0] == a:
            print('IS THIS YOUR ACCOUNT')
            c1 = f"SELECT fname, lname FROM user_accounts WHERE password='{b}'"
            cursor.execute(c1)
            data1 = cursor.fetchone()
            full_name = f"{data1[0]} {data1[1]}"

            x = ['FIRST NAME', 'LAST NAME', 'PHONE NUMBER', 'GENDER', 'DATE OF BIRTH', 'AGE']
            s1 = f"SELECT fname, lname, phno, gender, dob, age FROM user_accounts WHERE password='{b}'"
            cursor.execute(s1)
            account_data = cursor.fetchone()

            for i, label in enumerate(x):
                print(f"{label} ::: {account_data[i]}")

            print('1. YES')
            print('2. NO')
            vi = int(input('ENTER YOUR CHOICE: '))
            
            if vi == 1:
                delete_query = f"DELETE FROM user_accounts WHERE password='{b}'"
                cursor.execute(delete_query)
                return True
            else:
                print('RETRY')
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')


