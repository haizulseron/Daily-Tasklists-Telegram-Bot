from database.storage import (
    get_daily_tasks,
    save_daily_task,
    remove_daily_task,
    update_daily_task,
    toggle_daily_task_status,
    get_tasks,
    save_task
)
from bot import bot

def add_daily_task(message):
    task = message.text
    user_id = message.chat.id
    # Save the task as a daily task
    save_daily_task(user_id, task)
    # Also add it to today's task list
    save_task(user_id, task)
    bot.send_message(message.chat.id, "Daily task added and added to today's task list.")

def delete_daily_task(message):
    task_index = int(message.text) - 1
    user_id = message.chat.id
    remove_daily_task(user_id, task_index)
    bot.send_message(message.chat.id, "Daily task deleted.")

def edit_daily_task(message):
    user_id = message.chat.id
    task_index = int(message.text.split()[0]) - 1
    new_task = ' '.join(message.text.split()[1:])
    update_daily_task(user_id, task_index, new_task)
    bot.send_message(message.chat.id, "Daily task updated.")

def toggle_daily_task(message):
    task_index = int(message.text) - 1
    user_id = message.chat.id
    toggle_daily_task_status(user_id, task_index)
    bot.send_message(message.chat.id, "Daily task status toggled.")

def view_daily_tasks(message):
    user_id = message.chat.id
    daily_tasks = get_daily_tasks(user_id)
    if not daily_tasks:
        bot.send_message(message.chat.id, "No daily tasks found.")
        return
    response = "Daily Tasks:\n"
    for i, task in enumerate(daily_tasks, start=1):
        status = "✅" if task["enabled"] else "❌"
        response += f"{i}. {task['task']} {status}\n"
    bot.send_message(message.chat.id, response)

def reset_daily_tasks():
    users_tasks = get_tasks()
    for user_id, tasks in users_tasks.items():
        daily_tasks = get_daily_tasks(user_id)
        for daily_task in daily_tasks:
            if daily_task["enabled"]:
                save_task(user_id, daily_task["task"])
