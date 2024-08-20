import schedule
import time
from threading import Thread
from tasks.task_management import get_tasks, get_reminder_setting
from bot import bot

def send_reminders():
    users_tasks = get_tasks()
    for user_id, tasks in users_tasks.items():
        if get_reminder_setting(user_id):
            incomplete_tasks = [task for task in tasks if not task["completed"]]
            if incomplete_tasks:
                bot.send_message(user_id, "You have incomplete tasks. Don't forget to complete them!")

def start_scheduler():
    # Schedule reminders every 2 hours from 8:00 AM to 10:00 PM
    schedule.every().day.at("08:00").do(send_reminders)
    schedule.every().day.at("10:00").do(send_reminders)
    schedule.every().day.at("12:00").do(send_reminders)
    schedule.every().day.at("14:00").do(send_reminders)
    schedule.every().day.at("16:00").do(send_reminders)
    schedule.every().day.at("18:00").do(send_reminders)
    schedule.every().day.at("20:00").do(send_reminders)
    schedule.every().day.at("22:00").do(send_reminders)

    # Start a thread to run the scheduler
    def run_continuously():
        while True:
            schedule.run_pending()
            time.sleep(1)
    
    t = Thread(target=run_continuously)
    t.start()
