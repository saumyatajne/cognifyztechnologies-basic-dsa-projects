class Task:
    def __init__(self, task_id, description, status):
        self.task_id = task_id
        self.description = description
        self.status = status

class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, description, status="Incomplete"):
        task_id = len(self.tasks) + 1
        new_task = Task(task_id, description, status)
        self.tasks.append(new_task)
        print("Task created successfully.")

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
                print("Task updated successfully.")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully.")
                return
        print("Task not found.")

# Testing the application
if __name__ == "__main__":
    task_manager = TaskManager()
    
    # Create tasks
    task_manager.create_task("Complete assignment")
    task_manager.create_task("Buy groceries")
    
    # Read tasks
    task_manager.read_tasks()
    
    # Update task
    task_manager.update_task(1, "Complete project", "Complete")
    
    # Delete task
    task_manager.delete_task(2)
    
    # Read tasks after update and delete
    task_manager.read_tasks()
