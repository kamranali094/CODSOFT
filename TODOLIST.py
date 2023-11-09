class TDList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added successfully.')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed successfully.')
        else:
            print(f'Task "{task}" not found.')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks.')
        else:
            print('Tasks are:')
            for i, task in enumerate(self.tasks, 1):
                print(f'{i}. {task}')

def main():
    todo_list = TDList()

    while True:
        print('To-Do List Menu:')
        print('1. Add Task')
        print('2. Remove Task')
        print('3. View Tasks')
        print('4. Exit')

        choice = input()

        if choice == '1':
            task = input('Enter the task: ')
            todo_list.add_task(task)
        elif choice == '2':
            task = input('Enter the task to remove: ')
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            print('Goodbye!')
            break
        else:
            print('Invalid Dial')

if _name_ == "_main_":
    main()