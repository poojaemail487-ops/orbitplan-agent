# Routine Builder Agent
# Creates smart routines based on user's tasks and habits

class RoutineBuilder:
    def create_routine(self, tasks):
        morning = []
        afternoon = []
        evening = []

        for t in tasks:
            if t["priority"] == "High":
                morning.append(t["task"])
            elif t["category"] == "Health":
                evening.append(t["task"])
            else:
                afternoon.append(t["task"])

        return {
            "Morning Routine": morning,
            "Afternoon Routine": afternoon,
            "Evening Routine": evening
        }
