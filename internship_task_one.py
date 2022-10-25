import psycopg2

mycursor = None
conn = None
loop = 0

def features(data):
    while loop != 5:
        choice = int(input('choose the operation you would like to do \n 1:Insert data into users table \n 2: update email \n 3: delete user \n 4: view data \n 5: quit\n' ))
        if choice == 1:
            fn = input("enter first name\n")
            ln = input("enter last name\n")
            em = input("enter email \n")
            sal = int(input("enter salary\n"))
            tup=(fn,ln,em,sal)
            mycursor.execute(data,tup)

        elif choice == 2:
            us_id = input("enter user id to change the email id \n")
            mail = input("enter your active email id\n")
            tup = (mail,us_id)
            update_script = 'update users set email = %s where user_id = %s ;'
            mycursor.execute(update_script,tup)

        elif choice == 3:
            use_id= int(input('enter user id to delete the record\n'))
            delete_record = 'delete from users where user_id ={}'.format(use_id)
            mycursor.execute(delete_record)

        elif choice == 4:
            mycursor.execute('select * from users;')
            for i in mycursor.fetchall():
                print(i,'\n')

        elif choice == 5:
            return

        else:
            print("Wrong option choosed")

try:
    conn = psycopg2.connect(host="localhost", database="internship", user="postgres", password="postgresql@20", port=5432 )
    mycursor = conn.cursor()
    mycursor.execute("DROP TABLE users;")
    create_table = '''CREATE TABLE IF NOT EXISTS users(
                        user_id serial primary key,
                        first_name varchar(30),
                        last_name varchar(30),
                        email varchar(30) not null default 'No email provided',
                        amount int
                        ); '''
    mycursor.execute(create_table)

    # add data to the table % s is used as place holder for values -- we need to use single inverted commas for postgres
    data = ' INSERT INTO users( first_name, last_name, email, amount) values (%s,%s,%s,%s)'
    data_values = [( 'nagraj', 'gojanur', 'nagraj@gmail.com', 10000), ('sachin', 'usa', 'sachin@gmail.com', 13000)]

    for record in data_values:
        mycursor.execute(data,record)

    features(data)

    conn.commit()


except Exception as error:
    print("Error")

finally:
    if mycursor != None:
        mycursor.close()
    if conn != None:
        conn.close()