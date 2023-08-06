FILE_NAME= "todos.txt"


def read_todos(filename=FILE_NAME):
    with open(filename, 'r+') as read_file:
        get_todos = read_file.readlines()
    return get_todos


def write_todos(list_write_todos, filename=FILE_NAME):
    with open(filename, 'w+') as write_file:
        write_file.writelines(list_write_todos)


def action_add_todos(add_todo, filename=FILE_NAME):
    add_todo = add_todo.strip().capitalize() + "\n"

    with open(filename, 'a+') as add_file:
        add_file.write(add_todo)
