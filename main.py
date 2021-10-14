import argparse
parser = argparse.ArgumentParser('To Do app')
parser.add_argument("--create",type=str, nargs=1, action='store',help='create task')
parser.add_argument("--task-id",type=int , nargs=1,action='store',help="id of task")
parser.add_argument("--edit-title", nargs=2, action='store',help="title of task")
parser.add_argument("--edit-status", nargs=2, action='store',help="current status ")
parser.add_argument("--delete",type=int,nargs=1, action='store',help="delete "),
parser.add_argument("--list",nargs="*",action='store',help="current status ")
parser.add_argument("--search",type=str,nargs=1,action='store',help="search in title ")
parser.add_argument("--list-complete",action='store',help="current status ")
parser.add_argument("--list-incomplete",action='store',help="current status ")

args = parser.parse_args()
print(args)
# if __name__=="__main__":
#     pass