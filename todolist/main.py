# Python Todolist

# todolist
todolist = []

# Exit program
def exit_program():
    user_resp = input('Are you sure you want to exit? (y/n) ')
    if user_resp.strip().lower() == 'y':
        exit()

# Print todolist
def print_todolist():
    print('Todolist:')
    count = 1
    if len(todolist) == 0:
        print('You have to add some tasks!')
    else:
        for item in todolist:
            print(f'{count}. {item}')
            count += 1

# Edit task
def edit_task():
    print('Edit task:')

# Delete task
def delete_task():
    while True:
        task_to_remove = input('Enter the task number to remove or type \'c\' to cancel: ')
        if task_to_remove.strip().lower() == 'c':
            break
        else:
            try:
                num_remove = int(task_to_remove)
                if num_remove > len(todolist) or num_remove <= 0:
                    print('Invalid task. Try again.')
                else:
                    del todolist[num_remove - 1]
                    break
            except ValueError:
                print('Not a valid task number. Try again.')

# Add task
def add_task():
    new_task = input('Enter new task: ')
    confirm = input(f'Are you sure you want to add {new_task}? (y/n) ')
    if confirm.strip().lower() == 'y':
        todolist.append(new_task)
    else:
        print('Task not added.')

# Main options
def main_options():
        print('''\
        1. Add task
        2. Remove task
        3. Edit task
        4. Exit program''')
        user_resp = input('Enter your choice: ')
        match user_resp:
            case '1':
                add_task()
            case '2':
                if len(todolist) == 0:
                    print('You have to add some tasks!')
                else:
                    delete_task()
            case '3':
                edit_task()
            case '4':
                exit_program()
            case _:
                print('Invalid option. Try again.')

# Main Prompt: Add, delete, edit, exit
def main_prompt():
    while True:
        print_todolist()
        main_options()

def launch():
    main_prompt()

def main():
    launch()

if __name__ == '__main__':
    main()