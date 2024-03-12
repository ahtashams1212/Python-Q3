todos = [
    {'id': 1, 'task': 'Complete Advance Challange'},
    {'id': 2, 'task': 'of TODO'},
    {'id': 3, 'task': 'in Array'},
]

# 1st Function: Return All Todos
def get_all_todos():
    return todos

# 2nd Function: Return a Single Todo based on ID
def get_single_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            return todo
    return None  # Return None if todo with specified ID is not found

# 3rd Function: Takes a new Todo Data in Valid Format and Returns it
def add_new_todo(new_todo_data):
    if 'id' not in new_todo_data or 'task' not in new_todo_data:
        raise ValueError("Invalid todo data format. 'id' and 'task' are required.")
    
    new_todo = {'id': new_todo_data['id'], 'task': new_todo_data['task']}
    todos.append(new_todo)
    return new_todo

# 1. Get all todos
all_todos = get_all_todos()
print("All Todos:", all_todos)

# 2. Get a single todo by ID
todo_id_to_get = 2
single_todo = get_single_todo(todo_id_to_get)
print(f"Todo with ID {todo_id_to_get}:", single_todo)

# 3. Add a new todo
new_todo_data = {'id': 4, 'task': 'Read a book of Python'}
new_todo = add_new_todo(new_todo_data)
print("New Todo added:", new_todo)
print("Updated Todos:", todos)

