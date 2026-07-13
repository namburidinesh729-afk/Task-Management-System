import streamlit as st

from models import search_tasks

st.title("📋 View Tasks")

st.caption("Browse, search, filter, and export your tasks.")

st.divider()

search = st.text_input(
    label="Search Tasks",
    placeholder="🔍 Search by task title...",
)
st.caption("Filter your tasks")
col1, col2 = st.columns(2)

with col1:

    priority = st.selectbox(
        "Priority",
        [
            "All",
            "High",
            "Medium",
            "Low"
        ]
    )

with col2:

    status = st.selectbox(
        "Status",
        [
            "All",
            "Pending",
            "Completed"
        ]
    )

df = search_tasks(
    search,
    priority,
    status
)

df.columns = [
    "ID",
    "Title",
    "Description",
    "Priority",
    "Due Date",
    "Status"
]

if df.empty:
    st.info("📭 No matching tasks found.")
else:
    st.caption(f"📄 Showing {len(df)} task(s)")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📤 Download CSV",
        data=csv,
        file_name="tasks.csv",
        mime="text/csv",
        use_container_width=True
    )