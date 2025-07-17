from complete.storage import load_tasks,save_tasks
#add task 
def  add_task():
   tasks =load_tasks()
   task_id=len(tasks)+1
   task_title=input("Enter task title:")
   while not task_title:
      print("Title of the task is required")
      task_title=input("Enter task title:")

   task_description=input("Enter task description:")
   
   task_status=input("Enter Status of tasks:")
   while not task_status:
      print("Status of the task is required")
      task_status=input("Enter Status of tasks:")

   task_due_date=input("Enter Due Date (YYYY-MM-DD):")
   while not task_due_date:
      print("Due Date of the task is required")
      task_due_date=input("Enter Due Date (YYYY-MM-DD):")

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
    for task in tasks:
      if task["id"]==task_id:
          task["status"]="Completed"
          break
    save_tasks(tasks)
    print("Task Marked Complete Succesfully\n" \
    "" \
    "" \
    "")


#Delete Task
def del_task():
   tasks =load_tasks()
   task_id=int(input ("Enter Task ID to Delete the task:"))
   tasks=[task for task in tasks if task["id"]!=task_id]
   save_tasks(tasks)
   print("Task deleted Succesfully\n" \
   "" \
   "" \
   "")
    
