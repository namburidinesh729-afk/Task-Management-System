from datetime import date
from database import (
    execute_query,
    fetch_query,
    fetch_one,
    fetch_value,
    fetch_dataframe
)

def search_tasks(search, priority, status):

    query = """
    SELECT *

    FROM tasks

    WHERE title LIKE ?
    """

    values = [f"%{search}%"]

    if priority != "All":

        query += " AND priority=?"

        values.append(priority)

    if status != "All":

        query += " AND status=?"

        values.append(status)

    query += " ORDER BY due_date"

    return fetch_dataframe(
        query,
        tuple(values)
    )

def get_all_tasks():

    query = """
    SELECT *
    FROM tasks
    ORDER BY id DESC
    """

    return fetch_query(query)

def get_task_by_id(task_id):

    query = """
    SELECT *
    FROM tasks
    WHERE id = ?
    """

    return fetch_one(
        query,
        (task_id,)
    )

def update_task(
        task_id,
        title,
        description,
        priority,
        due_date,
        status
):

    query = """
    UPDATE tasks

    SET

    title=?,

    description=?,

    priority=?,

    due_date=?,

    status=?

    WHERE id=?
    """

    execute_query(
        query,
        (
            title,
            description,
            priority,
            due_date,
            status,
            task_id
        )
    )

def add_task(title, description, priority, due_date):

    query = """
    INSERT INTO tasks
    (title, description, priority, due_date)

    VALUES (?, ?, ?, ?)
    """

    execute_query(
        query,
        (
            title,
            description,
            priority,
            due_date
        )
    )

def delete_task(task_id):

    query = """
    DELETE FROM tasks
    WHERE id = ?
    """

    execute_query(
        query,
        (task_id,)
    )

def get_total_tasks():

    query = """
    SELECT COUNT(*)
    FROM tasks
    """

    return fetch_value(query)

def get_completed_tasks():

    query = """
    SELECT COUNT(*)

    FROM tasks

    WHERE status='Completed'
    """

    return fetch_value(query)

def get_pending_tasks():

    query = """
    SELECT COUNT(*)

    FROM tasks

    WHERE status='Pending'
    """

    return fetch_value(query)

def get_high_priority_tasks():

    query = """
    SELECT COUNT(*)

    FROM tasks

    WHERE priority='High'
    """

    return fetch_value(query)

def get_low_priority_tasks():

    query = """
    SELECT COUNT(*)
    FROM tasks
    WHERE priority='Low'
    """

    return fetch_value(query)

def get_medium_priority_tasks():

    query = """
    SELECT COUNT(*)
    FROM tasks
    WHERE priority='Medium'
    """

    return fetch_value(query)

def get_completion_percentage():

    total = get_total_tasks()

    if total == 0:
        return 0

    completed = get_completed_tasks()

    return round((completed / total) * 100)

def get_due_today():

    query = """
    SELECT COUNT(*)
    FROM tasks
    WHERE due_date=?
    """

    return fetch_value(
        query,
        (str(date.today()),)
    )


def get_overdue_tasks():

    query = """
    SELECT COUNT(*)
    FROM tasks
    WHERE due_date < ?
    AND status='Pending'
    """

    return fetch_value(
        query,
        (str(date.today()),)
    )

def get_recent_tasks():

    query = """
    SELECT title,
           priority,
           status

    FROM tasks

    ORDER BY id DESC

    LIMIT 5
    """

    return fetch_query(query)