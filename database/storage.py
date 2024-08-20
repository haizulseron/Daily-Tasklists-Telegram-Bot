import json
import os

DATA_PATH = "database/data.json"

def _load_data():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def _save_data(data):
    with open(DATA_PATH, 'w') as f:
        json.dump(data, f, indent=4)

def get_tasks(user_id):
    data = _load_data()
    return data.get(str(user_id), {}).get("tasks", [])

def save_task(user_id, task):
    data = _load_data()
    user_data = data.setdefault(str(user_id), {"tasks": [], "daily_tasks": [], "reminder": False})
    user_data["tasks"].append({"task": task, "completed": False})
    _save_data(data)

def remove_task(user_id, task_index):
    data = _load_data()
    user_data = data.get(str(user_id), {"tasks": []})
    user_data["tasks"].pop(task_index)
    _save_data(data)

def update_task(user_id, task_index, completed=None, new_task=None):
    data = _load_data()
    user_data = data.get(str(user_id), {"tasks": []})
    if completed is not None:
        user_data["tasks"][task_index]["completed"] = completed
    if new_task:
        user_data["tasks"][task_index]["task"] = new_task
    _save_data(data)

def toggle_reminder_setting(user_id):
    data = _load_data()
    user_data = data.setdefault(str(user_id), {"tasks": [], "daily_tasks": [], "reminder": False})
    user_data["reminder"] = not user_data["reminder"]
    _save_data(data)
    return user_data["reminder"]

def get_reminder_setting(user_id):
    data = _load_data()
    return data.get(str(user_id), {}).get("reminder", False)

# Daily tasks and other functions...

def get_daily_tasks(user_id):
    data = _load_data()
    return data.get(str(user_id), {}).get("daily_tasks", [])

def save_daily_task(user_id, task):
    data = _load_data()
    user_data = data.setdefault(str(user_id), {"tasks": [], "daily_tasks": []})
    user_data["daily_tasks"].append({"task": task, "enabled": True})
    _save_data(data)

def remove_daily_task(user_id, task_index):
    data = _load_data()
    user_data = data.get(str(user_id), {"tasks": [], "daily_tasks": []})
    user_data["daily_tasks"].pop(task_index)
    _save_data(data)

def update_daily_task(user_id, task_index, new_task):
    data = _load_data()
    user_data = data.get(str(user_id), {"tasks": [], "daily_tasks": []})
    user_data["daily_tasks"][task_index]["task"] = new_task
    _save_data(data)

def toggle_daily_task_status(user_id, task_index):
    data = _load_data()
    user_data = data.get(str(user_id), {"tasks": [], "daily_tasks": []})
    current_status = user_data["daily_tasks"][task_index]["enabled"]
    user_data["daily_tasks"][task_index]["enabled"] = not current_status
    _save_data(data)
