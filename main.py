from bot.handlers import bot, register_handlers
from scheduling.scheduler import start_scheduler

def main():
    register_handlers()
    start_scheduler()
    bot.polling(none_stop=True)

if __name__ == "__main__":
    main()
