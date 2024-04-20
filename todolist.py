class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task deleted successfully.")
        else:
            print("Task not found.")

    def update_task(self, task_index, new_task):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index] = new_task
            print("Task updated successfully.")
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")
        else:
            print("Your to-do list is empty.")


def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add task")
        print("2. Delete task")
        print("3. Update task")
        print("4. View task")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                task = input("Enter your task: ")
                todo_list.add_task(task)
            elif choice == 2:
                task_index = int(input("Enter index of the task to delete: ")) - 1
                todo_list.delete_task(task_index)
            elif choice == 3:
                task_index = int(input("Enter index of the task to update: ")) - 1
                new_task = input("Enter new task: ")
                todo_list.update_task(task_index, new_task)
            elif choice == 4:
                todo_list.view_tasks()
            elif choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
