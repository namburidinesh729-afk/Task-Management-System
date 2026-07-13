import streamlit as st
import plotly.express as px
import pandas as pd
from models import *
from utils import metric_card
with open("assets/style.css") as f:

    st.markdown(

        f"<style>{f.read()}</style>",

        unsafe_allow_html=True
    )
st.title("📊 Dashboard")

st.caption("Monitor your productivity and task insights.")

st.divider()

total = get_total_tasks()
completed = get_completed_tasks()
pending = get_pending_tasks()
high = get_high_priority_tasks()
medium = get_medium_priority_tasks()
low = get_low_priority_tasks()
progress = get_completion_percentage()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        metric_card("📋 Total Tasks", total, "#2563eb"),
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        metric_card("✅ Completed", completed, "#16a34a"),
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        metric_card("⌛ Pending", pending, "#f59e0b"),
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        metric_card("🔥 High Priority", high, "#dc2626"),
        unsafe_allow_html=True
    )

st.divider()

st.subheader("📈 Overall Progress")

st.progress(progress / 100)

col1, col2 = st.columns([1, 4])

with col1:
    st.metric("Progress", f"{progress}%")

with col2:
    if progress == 100:
        st.success("🎉 All tasks completed!")
    elif progress >= 75:
        st.success("Great work! You're almost done.")
    elif progress >= 50:
        st.info("You're making good progress.")
    elif progress >= 25:
        st.warning("Keep going! You're getting started.")
    else:
        st.error("Let's complete some tasks today!")

st.divider()

st.subheader("📈 Analytics")

chart1, chart2 = st.columns(2)

# ---------------- Pie Chart ----------------

with chart1:

    st.subheader("🥧 Status Distribution")

    status_df = pd.DataFrame(
        {
            "Status": [
                "Completed",
                "Pending"
            ],
            "Tasks": [
                completed,
                pending
            ]
        }
    )

    fig = px.pie(
        status_df,
        names="Status",
        values="Tasks",
        hole=0.45
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------- Bar Chart ----------------

with chart2:

    st.subheader("📊 Priority Distribution")

    priority_df = pd.DataFrame(
        {
            "Priority": [
                "High",
                "Medium",
                "Low"
            ],
            "Tasks": [
                high,
                medium,
                low
            ]
        }
    )

    bar = px.bar(
        priority_df,
        x="Priority",
        y="Tasks",
        text="Tasks"
    )

    st.plotly_chart(
        bar,
        use_container_width=True
    )

st.divider()

today, overdue = st.columns(2)

with today:

    st.metric(
        "📅 Due Today",
        get_due_today()
    )

with overdue:

    st.metric(
        "🚨 Overdue",
        get_overdue_tasks()
    )

st.divider()

st.subheader("🕒 Recently Added Tasks")

recent_tasks = get_recent_tasks()

if recent_tasks:

    for title, priority, status in recent_tasks:

        icon = "🔴"

        if priority == "Medium":
            icon = "🟡"

        elif priority == "Low":
            icon = "🟢"

        status_icon = "⏳"

        if status == "Completed":
            status_icon = "✅"

        st.write(
            f"{icon} **{title}**   {status_icon} {status}"
        )

else:

    st.info("📭 No tasks found.Create your first task from the Add Task page.")