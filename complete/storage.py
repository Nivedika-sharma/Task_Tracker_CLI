import json

#file to store tasks

Task_file='file/tasks.json'

def load_tasks():
    "Load Tasks from the JSON file."
    try:
        with open(Task_file,'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return[] # If the file does not exist return an empty List
    


#file to save tasks

def save_tasks(tasks):
    "Save Tasks to the JSON file."
    with open(Task_file,'w') as file:
        json.dump(tasks,file,indent=4)