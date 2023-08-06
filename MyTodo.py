import streamlit as st
from todofunctions import action_add_todos, write_todos, read_todos


def add_todo():
    new_todo = st.session_state["new_todo"]
    if not new_todo or new_todo != "":
        action_add_todos(new_todo)
    # st.session_state["new_todo"] = ""


todos = read_todos()

st.title("My To-Do App")

input_box = st.text_input(label="New To-Do", key="new_todo", max_chars=25, on_change=add_todo,
                          label_visibility="hidden", placeholder="Enter a new To-Do")

for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if st.session_state[todo] and st.session_state["delete"]:
        todos.remove(todo)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


done_button = st.button("Done", key="delete")
