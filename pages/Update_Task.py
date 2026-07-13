import streamlit as st
from models import (
    get_all_tasks,
    get_task_by_id,
    update_task
)

st.title("✏️ Update Task")      

st.caption("Modify the details of an existing task.")

st.divider()

# Get all tasks
tasks = get_all_tasks()

if not tasks:
    st.warning("No tasks available.")
    st.stop()

# Dropdown with better labels
task_dict = {
    f"{task[1]} • {task[3]} • {task[5]}": task[0]
    for task in tasks
}

selected_task = st.selectbox(
    "Select Task",
    list(task_dict.keys())
)

task_id = task_dict[selected_task]

# Fetch selected task
task = get_task_by_id(task_id)

st.divider()

# ---------------------------
# Task Information
# ---------------------------

st.subheader("📝 Task Information")

title = st.text_input(
    "Task Title",
    value=task[1]
)

description = st.text_area(
    "Description",
    value=task[2]
)

st.divider()

# ---------------------------
# Task Settings
# ---------------------------

st.subheader("⚙️ Task Settings")

col1, col2 = st.columns(2)

with col1:

    priority = st.selectbox(
        "Priority",
        ["High", "Medium", "Low"],
        index=["High", "Medium", "Low"].index(task[3])
    )

    status = st.selectbox(
        "Status",
        ["Pending", "Completed"],
        index=["Pending", "Completed"].index(task[5])
    )

with col2:

    due_date = st.date_input(
        "Due Date",
        value=task[4]
    )

st.divider()

if st.button("💾 Save Changes", use_container_width=True):

    if title.strip() == "":
        st.error("Task title cannot be empty.")

    else:

        update_task(
            task_id,
            title,
            description,
            priority,
            str(due_date),
            status
        )

        st.success("✅ Task updated successfully!")

        st.balloons()

        st.rerun()