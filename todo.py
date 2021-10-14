from connection import DBConnect
import main
from datetime import datetime

class Task(DBConnect):
    def __init__(self):
        DBConnect.__init__(self)

    #creating a task...........
    def insert_task(self,title):
        query="insert into task(title,created_at) values('{}','{}')".format(title[0],datetime.now())
        DBConnect.execute_query(self,query)
        self.con.commit()
        print("new task is created title {}".format(title))

    # udating the title of task
    def update_title(self,task_id,title):
        query="update task SET title = '{}',status='complete' where task_id ={} ".format(title,task_id)
        DBConnect.execute_query(self,query)
        self.con.commit()
        print("Title of task_id {} has been changed to {}".format(task_id,title))

    # updating status
    def update_status(self,task_id,status):
        query="update task set status='{}', completed_at='{}' where task_id='{}'".format(status,datetime.now().strftime("%Y-%m-%d %H:%M:%S"),int(task_id))
        DBConnect.execute_query(self,query)
        self.con.commit()
        print("task_id {} status has been changed to {}".format(task_id,status))

    #deleting the task
    def delete_task(self,task_id):
        query="delete from task where task_id={}".format(task_id)
        DBConnect.execute_query(self,query)
        self.con.commit()
        print("task_id {} is deleted".format(task_id))
    
    # listing all task
    def list_task(self):
        query="select*from task"
        DBConnect.execute_query(self,query)
        print("list of all tasks")
        for row in self.execute_query():
            print("Task_id:",row[0])
            print("Ttile:",row[1])
            print("created_at:",row[2])
            print("completed_at:",row[3])
            print("status:",row[4])
            print()  
       
    #printing list-complete
    def list_complete(self):
        query="select task_id,title,status from task where status='complete' "
        DBConnect.execute_query(self,query)
        print("List of completed task: ")
        for row in self.cur:
            print("Task_id:",row[0])
            print("Ttile:",row[1])
            print("status:",row[2])
            print()
            
    #printing list-incomplete
    def list_incomplete(self):
        query="select task_id,title,status from task where status='incomplete' "
        print("List of incompleted task: ")
        for row in self.cur:
            print("Task_id:",row[0])
            print("Ttile:",row[1])
            print("status:",row[2])
            print()
    # title search in title
    def title_search(self,title):
    
        query="select * from task where title like '%{}%'".format(title)
        DBConnect.execute_query(self,query)
        for row in self.cur:
            print("Task_id:",row[0])
            print("Matched title:",row[1])
            print()
   
#object of class list
connect=Task()
#create task
if main.args.create:
    connect.insert_task(main.args.create)

#list all task
elif main.args.list==[]:
    connect.list_task()

#complete list
elif main.args.list and main.args.list[0]=="complete":
    connect.list_complete()

#incoplete list
elif main.args.list and main.args.list[0]=="incomplete":
    connect.list_incomplete()

#editing title
elif main.args.edit_title:
    connect.update_title(main.args.edit_title[0],main.args.edit_title[1])

#updating status
elif main.args.edit_status: 
    connect.update_status(main.args.edit_status[0],main.args.edit_status[1])

#deleting task
elif main.args.delete:
    connect.delete_task(main.args.task_id)

# title search in title
elif main.args.search:
    connect.title_search(main.args.search[0])
