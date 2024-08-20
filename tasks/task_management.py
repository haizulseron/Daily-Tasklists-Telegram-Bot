from database.storage import (
    get_tasks,
    save_task,
    remove_task,
    update_task,
    toggle_reminder_setting
)
from bot import bot

def add_task(message):
    task = message.text
    user_id = message.chat.id
    save_task(user_id, task)
    bot.send_message(message.chat.id, "Task added.")

def delete_task(message):
    task_index = int(message.text) - 1
    user_id = message.chat.id
    remove_task(user_id, task_index)
    bot.send_message(message.chat.id, "Task deleted.")

def view_tasks(message):
    user_id = message.chat.id
    tasks = get_tasks(user_id)
    if not tasks:
        bot.send_message(message.chat.id, "No tasks found.")
        return
    response = "Tasks:\n"
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task["completed"] else "❌"
        response += f"{i}. {task['task']} {status}\n"
    bot.send_message(message.chat.id, response)

def complete_task(message):
    task_index = int(message.text) - 1
    user_id = message.chat.id
    update_task(user_id, task_index, completed=True)
    bot.send_message(message.chat.id, "Task marked as completed.")

def complete_all_tasks(message):
    user_id = message.chat.id
    tasks = get_tasks(user_id)
    for i in range(len(tasks)):
        update_task(user_id, i, completed=True)
    bot.send_message(message.chat.id, "All tasks have been marked as completed.")

def undo_complete_task(message):
    task_index = int(message.text) - 1
    user_id = message.chat.id
    update_task(user_id, task_index, completed=False)
    bot.send_message(message.chat.id, "Task marked as not completed.")

def edit_task(message):
    user_id = message.chat.id
    task_index = int(message.text.split()[0]) - 1
    new_task = ' '.join(message.text.split()[1:])
    update_task(user_id, task_index, new_task=new_task)
    bot.send_message(message.chat.id, "Task updated.")

def toggle_reminders(message):
    user_id = message.chat.id
    current_setting = toggle_reminder_setting(user_id)
    if current_setting:
        bot.send_message(user_id, "Reminders are now enabled.")
    else:
        bot.send_message(user_id, "Reminders are now disabled.")
