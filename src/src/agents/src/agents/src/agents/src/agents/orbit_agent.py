# OrbitPlan Master Agent
# Connects Task Analyzer + Reminder Agent + Routine Builder

from .task_analyzer import TaskAnalyzer
from .reminder_agent import ReminderAgent
from .routine_builder import RoutineBuilder

class OrbitAgent:
    def __init__(self):
        self.analyzer = TaskAnalyzer()
        self.reminders = ReminderAgent()
        self.routine_builder = RoutineBuilder()
        self.tasks = []

    def add_task(self, text, reminder_time=None):
        # Step 1: Analyze task
        analyzed = self.analyzer.analyze(text)
        self.tasks.append(analyzed)

        # Step 2: Add reminder (optional)
        if reminder_time:
            self.reminders.add_reminder(text, reminder_time)

        return analyzed

    def build_daily_routine(self):
        # Step 3: Build routine from all tasks
        return self.routine_builder.create_routine(self.tasks)

    def get_all_reminders(self):
        return self.reminders.get_all_reminders()

