import streamlit as st

from config import APP_TITLE, PAGE_ICON, LAYOUT

from database import create_table


st.set_page_config(

    page_title=APP_TITLE,

    page_icon=PAGE_ICON,

    layout=LAYOUT

)

create_table()

st.title("📝 Task Manager Pro")

st.header("Organize your work. Track your progress. Stay productive.")

st.write(
    """
Welcome to **Task Manager Pro**, a modern task management application built with Python and Streamlit.
"""
)

st.subheader("🚀 Features")

st.markdown(
    """
- ✅ Create, update and delete tasks
- 📊 Interactive dashboard
- 📈 Progress tracking
- 🔍 Search and filter tasks
- 📤 Export tasks to CSV
- 📅 Due today & overdue tracking
"""
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.info("📋 Use the sidebar to manage your tasks.")

with col2:
    st.success("🚀 Your productivity starts here!")

st.divider()
st.caption(
    "Built using Python • Streamlit • SQLite"
)    