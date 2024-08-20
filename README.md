# Using pyTelegramBotAPI

Personally, I always needed reminders when it comes to my daily tasks and I need to have a routine set of tasks to complete each day. I created this telegram bot in order to send reminders daily as well as set your daily tasks or custom tasks for that day.

This is so you can deploy this bot on your own using your own BOT from BOT_Father.

Was created using pyTelegramBotAPI (https://pypi.org/project/pyTelegramBotAPI/)

## Features
- Add Task
    - This allows you to add whatever task you want on a day by day basis
- Edit Task
- Delete Task
- View Tasks
- Toggle Reminders
- Daily Tasks Management
    - Daily Tasks when enabled, will allow your daily tasks to be in the main task list everyday at 12AM so you will have a routine set of tasks to complete everyday
    - Edit Daily Tasks
    - Add Daily Tasks
    - View Daily Tasks
    - Toggle Daily Tasks
    - Delete Daily Tasks
- Complete all tasks
- Reverse Completion of task

Setup

1. Goto https://telegram.me/BotFather, add a new bot, remember the API Token.


2. Clone the repository and navigate to the project directory.

```shell
git clone https://github.com/haizulseron/Daily-Tasklists-Telegram-Bot.git
cd Daily-Tasklist-Telegram-Bot
```

3. Edit config.py file

```bash
BOT_TOKEN = os.getenv('BOT_TOKEN', 'YOUR BOT TOKEN HERE')
```

Replace "YOUR BOT TOKEN HERE" with your API Token.

4. Create a virtual environment:
```shell
python -m venv venv
```

5. Activate the virtual environment:
```shell
source venv/bin/activate
```

6. Install the dependencies using 'requirements.txt' file:
```shell
pip install -r requirements.txt
```

7. Use the following to start the bot:

```
python3 main.py
```

or

```
python main.py
```