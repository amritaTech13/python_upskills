
# list = []
tasks = []
while True:
    print('--Todo-List--')
    print('1.Add Task')
    print('2.Remove task')
    print('3.show task')
    print('4.Exit')
    n = int(input('select choice 1-4 : '))

    def add_task():
        task = input("Enter task you want to add in your todo list: ")
        tasks.append(task)
        print(f"Task '{task}' added.")

    def remove_task():
        remove_no = int(input("Enter no of task to remove: "))
        if not tasks:
            print("No task found")
        else:    
            removed  = tasks.pop(remove_no-1)
            print(f"Removed task: {removed}")

    def show_task():  
        if not tasks:
            print("Task is empty")
        for i, task in enumerate(tasks, start=1):
            print("Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")



    if n == 1:
        add_task()
    elif n == 2:
        remove_task()
    elif n == 3:
        show_task()    
    elif n == 4:
        print('Exit')
        break
    else:
        print("PLease enter valid choice 1 to 4")    






