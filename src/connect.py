import mysql.connector as mysqlcon

#connection to mysql ------------------------------------------------------------------------------------------
try:            
    mydb = mysqlcon.connect(host = "127.0.0.1" ,user = "root" , password = "" ,database = "test")
        
    if mydb.is_connected():
        print("Database connected successfully!")

except mysqlcon.Error as err:
    print(f'Error connecting to database :{err}')

#create table ------------------------------------------------------------------------------------------    
def create_table(table_name):
   
    try:
        mytable = mydb.cursor()
                    
        mytable.execute(f"""create table if not exists {table_name}(
                        id int auto_increment primary key,
                        Fajr boolean,
                        Sunrise boolean,
                        Dhuhr boolean,
                        Asr boolean,
                        Maghrib boolean,
                        Isha boolean,
                        time timestamp default current_timestamp
                        )""")
        print("Table created successfully!")
            
    except mysqlcon.Error as err:
        print(f'Error creating table :{err}')
        

#insert data ------------------------------------------------------------------------------------------
def insert_data(table_name):
    try:
        mytable = mydb.cursor()
        
        mytable.execute(f"""insert into {table_name}(Fajr,Sunrise,Dhuhr,Asr,Maghrib,Isha)
                        values(0,0,0,0,0,0)""")
        print("Data inserted successfully!")
        mydb.commit()
    except mysqlcon.Error as err:
        print(f'Error inserting data :{err}')
    
 
#update data ------------------------------------------------------------------------------------------ 
def update_to_tb(salat_name,table_name,confirm=False):
    if confirm:
        try:
            mytable = mydb.cursor()
            mytable.execute(f"""update {table_name}
                                    set {salat_name} = 1
                                    where id =(select max(id) from {table_name})""")
            mydb.commit()
        except mysqlcon.Error as err:
            print(f'Error updating data :{err}')
            
           
Ntable = "test4"   
confirm = True         
update_to_tb("Sunrise",Ntable,confirm)
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------       
             
# mytable = mydb.cursor()


# mytable.execute("select * from data")

# result = mytable.fetchall()

# for i in result:
#     print(i)

# def connection(dname):
#     mydb = mysqlcon.connect(host = "127.0.0.1" ,user = "simitry" , password = "12345" ,database = "dname")



# mytable = mydb.cursor()
# mytable.execute("select nomid from test3")
# result = mytable.fetchall()
# for elem in result:
#     print(elem[0])