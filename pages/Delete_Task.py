import streamlit as st

from models import (
    get_all_tasks,
    delete_task
)

st.title("🗑 Delete Task")

st.caption("Remove tasks that are no longer needed.")

st.divider()

tasks = get_all_tasks()

if not tasks:

    st.warning("No Tasks Available.")

    st.stop()

task_dict = {
    f"{task[1]} • {task[3]} • {task[5]}": task[0]
    for task in tasks
}

selected = st.selectbox(
    "Select Task",
    list(task_dict.keys())
)

task_id = task_dict[selected]

st.warning("⚠ This action cannot be undone.")

if st.button(
    "🗑 Permanently Delete",
    use_container_width=True
):

    delete_task(task_id)

    st.success("Task Deleted Successfully!")

    st.rerun()