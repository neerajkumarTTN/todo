import mysql.connector as connector

#connection to mySQL database
class DBConnect:
    def __init__(self):
        self.con=connector.connect( host="localhost",
                        user="neeraj",
                        port=3306,
                        password="password",
                        database="tododatabase",
                        auth_plugin='mysql_native_password')


        if self.con.is_connected():
            print("Successfully connected to database.....")
            query='create table if not exists task ( task_id INT not null primary key auto_increment,title varchar(200) unique, created_at datetime  , completed_at datetime  , status varchar(20) default "incomplete")'
            cur=self.con.cursor()
            cur.execute(query)
        else:
            print("Some conectivity issue.....")

    @staticmethod
    def execute_query(self,query):
        cur=self.con.cursor()
        cur.execute(query)
    


