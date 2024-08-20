from bot import bot
from bot.keyboards import main_menu, task_management_menu
from tasks.task_management import (
    add_task,
    delete_task,
    view_tasks,
    complete_task,
    edit_task,
    complete_all_tasks,
    undo_complete_task,
    toggle_reminders,
)
from tasks.daily_tasks import (
    add_daily_task,
    delete_daily_task,
    edit_daily_task,
    toggle_daily_task,
    view_daily_tasks
)
from bot.utils import is_number

def register_handlers():
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(message.chat.id, "Welcome to the Accountability Bot!", reply_markup=main_menu())

    @bot.message_handler(commands=['add_task'])
    def handle_add_task(message):
        msg = bot.send_message(message.chat.id, "What is the task?")
        bot.register_next_step_handler(msg, process_add_task)

    def process_add_task(message):
        add_task(message)

    @bot.message_handler(commands=['delete_task'])
    def handle_delete_task(message):
        view_tasks(message)
        msg = bot.send_message(message.chat.id, "Which task number do you want to delete?")
        bot.register_next_step_handler(msg, process_delete_task)

    def process_delete_task(message):
        if is_number(message.text):
            delete_task(message)
        else:
            bot.send_message(message.chat.id, "Invalid input. Please enter the task number.")

    @bot.message_handler(commands=['view_tasks'])
    def handle_view_tasks(message):
        view_tasks(message)

    @bot.message_handler(commands=['complete_task'])
    def handle_complete_task(message):
        view_tasks(message)
        msg = bot.send_message(message.chat.id, "Which task number do you want to mark as completed?")
        bot.register_next_step_handler(msg, process_complete_task)

    def process_complete_task(message):
        if is_number(message.text):
            complete_task(message)
        else:
            bot.send_message(message.chat.id, "Invalid input. Please enter the task number.")

    @bot.message_handler(commands=['complete_all_tasks'])
    def handle_complete_all_tasks(message):
        complete_all_tasks(message)
        bot.send_message(message.chat.id, "All tasks have been marked as completed.")

    @bot.message_handler(commands=['undo_complete_task'])
    def handle_undo_complete_task(message):
        view_tasks(message)
        msg = bot.send_message(message.chat.id, "Which task number do you want to undo completion for?")
        bot.register_next_step_handler(msg, process_undo_complete_task)

    def process_undo_complete_task(message):
        if is_number(message.text):
            undo_complete_task(message)
        else:
            bot.send_message(message.chat.id, "Invalid input. Please enter the task number.")

    @bot.message_handler(commands=['edit_task'])
    def handle_edit_task(message):
        view_tasks(message)
        msg = bot.send_message(message.chat.id, "Enter the task number followed by the new task details (e.g., '1 New task').")
        bot.register_next_step_handler(msg, process_edit_task)

    def process_edit_task(message):
        if is_number(message.text.split()[0]):
            edit_task(message)
        else:
            bot.send_message(message.chat.id, "Invalid input. Please enter the task number followed by the new task details.")

    @bot.message_handler(commands=['toggle_reminders'])
    def handle_toggle_reminders(message):
        toggle_reminders(message)
        bot.send_message(message.chat.id, "Reminder setting updated.")

    # Handlers for managing daily tasks
    @bot.message_handler(commands=['manage_daily_tasks'])
    def handle_manage_daily_tasks(message):
        bot.send_message(message.chat.id, "Managing Daily Tasks", reply_markup=task_management_menu())

    @bot.message_handler(commands=['add_daily_task'])
    def handle_add_daily_task(message):
        msg = bot.send_message(message.chat.id, "What is the daily task?")
        bot.register_next_step_handler(msg, process_add_daily_task)

    def process_add_daily_task(message):
        add_daily_task(message)

    @bot.message_handler(commands=['delete_daily_task'])
    def handle_delete_daily_task(message):
        view_daily_tasks(message)
        msg = bot.send_message(message.chat.id, "Which daily task number do you want to delete?")
        bot.register_next_step_handler(msg, process_delete_daily_task)

    def process_delete_daily_task(message):
        if is_number(message.text):
            delete_daily_task(message)
        else:
            bot.send_message(message.chat.id, "Invalid input. Please enter the daily task number.")

    @bot.message_handler(commands=['edit_daily_task'])
    def handle_edit_daily_task(message):
        view_daily_tasks(message)
        msg = bot.send_message(message.chat.id, "Enter the daily task number followed by the new task details (e.g., '1 New daily task').")
        bot.register_next_step_handler(msg, process_edit_daily_task)

    def process_edit_daily_task(message):
        if is_number(message.text.split()[0]):
            edit_daily_task(message)
        else:
            bot.send_message(message.chat.id, "Invalid input. Please enter the daily task number followed by the new task details.")

    @bot.message_handler(commands=['toggle_daily_task'])
    def handle_toggle_daily_task(message):
        view_daily_tasks(message)
        msg = bot.send_message(message.chat.id, "Which daily task number do you want to toggle?")
        bot.register_next_step_handler(msg, process_toggle_daily_task)

    def process_toggle_daily_task(message):
        if is_number(message.text):
            toggle_daily_task(message)
        else:
            bot.send_message(message.chat.id, "Invalid input. Please enter the daily task number.")

    @bot.message_handler(commands=['view_daily_tasks'])
    def handle_view_daily_tasks(message):
        view_daily_tasks(message)

    # Back to main menu
    @bot.message_handler(commands=['back'])
    def handle_back(message):
        bot.send_message(message.chat.id, "Returning to main menu.", reply_markup=main_menu())
