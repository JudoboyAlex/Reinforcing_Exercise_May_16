class Task:

    def __init__(self,description, due_date):
        self.description = description
        self.due_date = due_date

    def __repr__(self):
        return "{},{}".format(self.description, self.due_date)
    
    def __str__(self):
        return "{},{}".format(self.description, self.due_date)

class TodoList:

    def __init__(self, tasks):
        self.tasks = tasks
    
    task_list = []
    
    @classmethod
    def add_task(cls, todo):
        cls.task_list.append(todo)


judo = Task("smash them up", "next week")
coding = Task("code like crazy", "tomorrow")
watch_Raptors = Task("go Raptors go!", "tonight!")

TodoList.add_task(judo)
print(TodoList.task_list)
TodoList.add_task(coding)
print(TodoList.task_list)
TodoList.add_task(watch_Raptors)
print(TodoList.task_list)

