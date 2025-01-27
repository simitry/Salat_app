import mysql.connector as mysqlcon

def connect_to_db(pwd, dname):
    try:            
        mydb = mysqlcon.connect(host = "127.0.0.1" ,user = "simitry" , password = pwd ,database = dname)
        
        if mydb.is_connected():
            print("Database connected successfully!")

    except mysqlcon.Error as err:
        print(f'error {err}')
    

# mytable = mydb.cursor()


# mytable.execute("select * from data")

# result = mytable.fetchall()

# for i in result:
#     print(i)

# def connection(dname):
#     mydb = mysqlcon.connect(host = "127.0.0.1" ,user = "simitry" , password = "12345" ,database = "dname")