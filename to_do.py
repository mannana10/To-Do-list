import datetime

class Database:
    entries = []

    def add_to_db(self,todo):
        self.entries.append(todo)
        print("ახალი შესასრულებელი სამუშაო წარმატებით დაემატა სიაში!")
    
    def show_todos(self):
        return self.entries
    
    def replace_todo_db(self, oldTodoIndex, newTodo):
        self.entries[oldTodoIndex] = newTodo
        print("შესასრულებელი სამუშაო წარმატებით შეიცვალა!")
    
    def delete_todo_db(self, todoIndex):
        self.entries.pop(todoIndex)
        print("შესასრულებელი სამუშაო წარმატებით ამოიშალა სიიდან!")


class Manager:

    def __init__(self, database):
        self.database = database

    def add(self, todo):
        self.database.add_to_db(todo)
    
    def showAll(self):
        data = self.database.show_todos()

        if data:
            for index, item in enumerate(data, 1):
                print(f"{'-'*25} {index} {'-'*25}" )
                print(item)
                print("-"*53)
        else:
            print("შესასრულებელი სამუშაოების სია ცარიელია!")
    
    def replace_todo(self, oldTodoIndex, newTodo):
        self.database.replace_todo_db(oldTodoIndex, newTodo)

    def delete_todo(self, todoIndex):
        self.database.delete_todo_db(todoIndex)



class ToDo:

    def __init__(self,text, deadline):
        self.text = text
        self.date = datetime.datetime.now()
        self.deadline = deadline

    def __str__(self):
        return f"Date : {self.date.strftime('%d/%m/%Y %H:%M')} \nშესასრულებელი სამუშაო : {self.text} \nბოლო ვადა :{self.deadline}"
    


def todo_checker(manager):
    while True:
        manager.showAll()
        oldTodoIndex = input("აირჩიეთ შესაცვლელი ან წასაშლელი ობიექტის ნომერი ")
        if not oldTodoIndex.isdigit():
            print("გთხოვთ შეიტანოთ რიცხვითი მნიშვნელობა!")
            continue
        oldTodoIndex = int(oldTodoIndex)
        if oldTodoIndex > len(manager.database.entries) or oldTodoIndex < 1:
            print(f"გთხოვთ შეიყვანოთ რიცხვი 1 - {len(manager.database.entries)} შუალედში!")
            continue

        oldTodoIndex = oldTodoIndex - 1
        return oldTodoIndex


def menu():
    choice = None
    database = Database()
    manager = Manager(database)

    while choice !="გ":
        print("მენიუ")
        print("დ - დამატება;")
        print("ჩ - ჩვენება;")
        print("შ - შეცვლა;")
        print("წ - წაშლა;")
        print("გ - პროგრამიდან გასვლა;")

        choice = input("მიუთითეთ რომელი მოქმედების განხორციელება გსურთ :").strip()

        if choice == "დ":
            text = input("შეიტანეთ შესასრულებელი სამუშაოს დასახელება : ").strip()
            deadline = input("შეიტანეთ სამუშაოს შესრულების ბოლო თარიღი :").strip()
            todo = ToDo(text, deadline)
            manager.add(todo)

        elif choice == "ჩ":
            manager.showAll()

        elif choice == "შ":
            if database.entries:
                oldTodoIndex = todo_checker(manager)
            text = input("შეიტანეთ შესასრულებელი სამუშაო, რომლითაც გსურთ არსებულის ჩანაცვლება : ").strip()
            deadline = input("შეიტანეთ შეცვლილი სამუშაოს შესრულების ბოლო თარიღი :").strip()
            newTodo = ToDo(text,deadline)
            manager.replace_todo(oldTodoIndex,newTodo)
            
        elif choice == "წ":
            if database.entries:
                todoIndex = todo_checker(manager)
                manager.delete_todo(todoIndex)
            else:
                print("შესასრულებელი სამუშაოების სია ცარიელია!")
        
        else:
            pass

menu()
