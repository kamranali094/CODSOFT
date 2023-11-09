class TDList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added successfully.')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks found.')
        else:
            print('Tasks:')
            for i, task in enumerate(self.tasks, 1):
                print(f'{i}. {task}')
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed successfully.')
        else:
            print(f'Task "{task}" not found.')

def main():
    todo_list = TDList()

    while True:
        print('To-Do List Menu:')
        print('1. Add Task')
        print('2. Remove Task')
        print('3. View Tasks')
        print('4. Exit')

        choice = input("")
        if choice == '1':
            task = input('Enter the task: ')
            todo_list.add_task(task)
        elif choice == '2':
            task = input('Enter the task to remove: ')
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            print('Exiting the program. Goodbye!')
            break
        else:
            print('Inavlid Dial')

main()
