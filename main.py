from task_tracker import add_task, list_tasks,update_task,del_task

def main():
    while True:
        print("========Welcome To Task Tracker==========")
        choice = input("Enter 1 : To Add Task" \
        "\nEnter 2 : To List all Task" \
        "\nEnter 3: To Update a Task" \
        "\nEnter 4: To Delete a Task"
        "\nEnter 5: To Exit from Task Tracker\n")

        if(choice=="1"):
            add_task()
        elif(choice=="2"):
            list_tasks()
        elif(choice=="3"):
            update_task()
        elif(choice=="4"):
            del_task()
        elif(choice=="5"):
            print("Exiting...")
            break
        else:
            print("Invalid Choice , Please try again\n")
if __name__ == "__main__":
        main()