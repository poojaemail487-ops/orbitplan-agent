# Reminder Agent
# Stores reminders and prepares them for notifications (future feature)

class ReminderAgent:
    def __init__(self):
        self.reminders = []

    def add_reminder(self, task, time):
        reminder = {
            "task": task,
            "time": time
        }
        self.reminders.append(reminder)
        return f"Reminder added: {task} at {time}"

    def get_all_reminders(self):
        return self.reminders
