# Task Analyzer Agent
# This agent reads user tasks and classifies them by priority, category, and effort.

class TaskAnalyzer:
    def analyze(self, task_text):
        # Simple rule-based logic (later we replace with LLM agent)
        task = task_text.lower()

        if "study" in task:
            category = "Learning"
        elif "project" in task:
            category = "Work"
        elif "health" in task or "exercise" in task:
            category = "Health"
        else:
            category = "General"

        # Basic priority logic
        if "urgent" in task or "today" in task:
            priority = "High"
        else:
            priority = "Medium"

        return {
            "task": task_text,
            "category": category,
            "priority": priority
        }
