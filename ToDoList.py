import random
def show_menu():
    print("Todo List Menu:")
    print("1. View:")
    print("2. Add:")
    print("3. Mark as Completed:")
    print("4. Delete: ")
    print("5. Quit")

def view_todo_list(todo_list):
    print("\nTodo List:")
    if not todo_list:
        print("No tasks in the list.")
    else:
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_todo(todo_list):
    task = input("\nEnter the task to add: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the Todo List.")

def mark_completed(todo_list):
    view_todo_list(todo_list)
    try:
        index = int(input("\nEnter the number of the completed task: ")) - 1
        completed_task = todo_list.pop(index)
        print(f"Task '{completed_task}' marked as completed.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid task number.")

# Define a function to delete a task from the to-do list
def delete_todo(todo_list):
    view_todo_list(todo_list)
    try:
        index = int(input("\nEnter the number of the task to delete: ")) - 1
        deleted_task = todo_list.pop(index)
        print(f"Task '{deleted_task}' deleted.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid task number.")

def main():
    todo_list = []

    while True:
        show_menu()
        ch = input("\nEnter Your Choice (1-5): ")

        if ch == '1':
            view_todo_list(todo_list)
        elif ch == '2':
            add_todo(todo_list)
        elif ch == '3':
            mark_completed(todo_list)
        elif ch == '4':
            delete_todo(todo_list)
        elif ch == '5':
            print("Exiting Todo List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()