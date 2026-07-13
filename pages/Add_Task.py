import streamlit as st

from models import add_task


st.title("➕ Add Task")

st.caption("Create a new task and organize your work.")

st.divider()

with st.form("task_form"):

    title = st.text_input("Task Title")

    description = st.text_area("Description")

    priority = st.selectbox(
        "Priority",
        ["High", "Medium", "Low"]
    )

    due_date = st.date_input("Due Date")

    submitted = st.form_submit_button("➕ Create Task")

    if submitted:

        if title.strip() == "":

            st.error("Task Title cannot be empty!")

        else:

            add_task(
                title,
                description,
                priority,
                str(due_date)
            )

            st.success("Task Added Successfully!")