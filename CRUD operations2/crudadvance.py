class Task:
    def __init__(self, task_id, description, status):
        self.task_id = task_id
        self.description = description
        self.status = status

class TaskManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = []

    def load_tasks(self):
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    task_id, description, status = line.strip().split(',')
                    self.tasks.append(Task(int(task_id), description, status))
            print("Tasks loaded successfully.")
        except FileNotFoundError:
            print("File not found. Creating a new file.")

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.task_id},{task.description},{task.status}\n")
        print("Tasks saved successfully.")

    def create_task(self, description, status="Incomplete"):
        task_id = len(self.tasks) + 1
        new_task = Task(task_id, description, status)
        self.tasks.append(new_task)
        self.save_tasks()

    def read_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("Tasks:")
        for task in self.tasks:
            print(f"ID: {task.task_id}, Description: {task.description}, Status: {task.status}")

    def update_task(self, task_id, new_description, new_status):
        for task in self.tasks:
            if task.task_id == task_id:
                task.description = new_description
                task.status = new_status
                self.save_tasks()
                print("Task updated successfully.")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print("Task deleted successfully.")
                return
        print("Task not found.")

# Testing the application
if __name__ == "__main__":
    file_path = "tasks.txt"
    task_manager = TaskManager(file_path)
    task_manager.load_tasks()
    
    task_manager.create_task("Complete assignment")
    task_manager.create_task("Buy groceries")
    task_manager.read_tasks()
    
    task_manager.update_task(1, "Complete project", "Complete")
    task_manager.delete_task(2)
    
    task_manager.read_tasks()
