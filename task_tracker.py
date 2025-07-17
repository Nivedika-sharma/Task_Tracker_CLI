from complete.storage import load_tasks,save_tasks
from datetime import datetime
#add task 
def  add_task():
   tasks =load_tasks()
   task_id=len(tasks)+1
   task_title=input("Enter task title:")
   while not task_title:
      print("Title of the task is required")
      task_title=input("Enter task title:")

   task_description=input("Enter task description:")
   
   task_status=input("Enter Status of tasks (Completed/Pending):")
   while not task_status:
      print("Status of the task is required")
      task_status=input("Enter Status of tasks:")

   while True:
    task_due_date=input("Enter Due Date (YYYY-MM-DD):")
    try:
       datetime.strptime(task_due_date,"%Y-%m-%d")
       break
    except:
       print("Invalid date format , Enter again")
   
    

   tasks.append(
      {
      "id":task_id,
      "title":task_title,
      "description":task_description,
      "status":task_status,
      "due_date":task_due_date
   
      }
    )
   save_tasks(tasks)
   print("Task added succesfully\n" \
   "" \
   "" \
   "" \
   "")

#To fetch due date
def get_date(tasks):
   return tasks['due_date']

#List All Task  
def list_tasks():
   tasks=load_tasks()
   tasks.sort(key=get_date,reverse=True)
  
   if tasks:
        print("+--+------------------------------------------------+----------------------------------------------------+----------------+----------------+")
        print("|ID|                 Task Title                     |                   Task Description                 |    Due_Date    |     Status     |")
        print("+--+------------------------------------------------+----------------------------------------------------+----------------+----------------+")
        for task in tasks:
         print("|{:<2}|{:<48}|{:<52}|{:<16}|{:<16}|".format(
            task['id'],task['title'],task['description'],task['due_date'],task['status']))
         print("+--+------------------------------------------------+----------------------------------------------------+----------------+----------------+")
   else:
      print("No Task Found\n" \
      "" \
      "" \
      "" \
      "")

#Update task
def update_task():
    tasks =load_tasks()
    task_id=int(input ("Enter Task ID to update the task:"))
    f=False
    for task in tasks:
      if task["id"]==task_id:
          task["status"]="Completed"
          f=True
          break
    if(f):     
      save_tasks(tasks)
      print("Task Marked Complete Succesfully\n" \
      "" \
      "" \
      "")
    else:
      print("No Task Found\n" \
      "" \
      "" \
      "" \
      "")


#Delete Task
def del_task():
   tasks =load_tasks()
   task_len=len(tasks)
   task_id=int(input ("Enter Task ID to Delete the task:"))
   tasks=[task for task in tasks if task["id"]!=task_id]
   if len(tasks)<task_len:
      save_tasks(tasks)
      print("Task deleted Succesfully\n" \
      "" \
      "" \
      "")
   else:
      print("No Task Found\n" \
      "" \
      "" \
      "" \
      "")

    
