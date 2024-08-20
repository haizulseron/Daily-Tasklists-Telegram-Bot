from telebot import types

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('/add_task', '/delete_task')
    markup.row('/view_tasks', '/complete_task')
    markup.row('/edit_task', '/complete_all_tasks')
    markup.row('/undo_complete_task', '/toggle_reminders')
    markup.row('/manage_daily_tasks')
    return markup

def task_management_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('/add_daily_task', '/delete_daily_task')
    markup.row('/edit_daily_task', '/toggle_daily_task')
    markup.row('/view_daily_tasks', '/back')
    return markup
