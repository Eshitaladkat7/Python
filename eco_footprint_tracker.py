import json
import matplotlib.pyplot as plt # type: ignore
from datetime import datetime

class EcoFootprintTracker:
    def __init__(self):
        self.activities = []

    def add_activity(self, activity, carbon_footprint):
        self.activities.append({
            'activity': activity,
            'carbon_footprint': carbon_footprint,
            'timestamp': datetime.now().isoformat()
        })

    def calculate_total_footprint(self):
        return sum(activity['carbon_footprint'] for activity in self.activities)

    def visualize_footprint(self):
        activities = [activity['activity'] for activity in self.activities]
        footprints = [activity['carbon_footprint'] for activity in self.activities]

        plt.bar(activities, footprints, color='green')
        plt.xlabel('Activities')
        plt.ylabel('Carbon Footprint (kg CO2)')
        plt.title('Eco-footprint Tracker')
        plt.show()

    def save_to_file(self, filename='eco_footprint.json'):
        with open(filename, 'w') as f:
            json.dump(self.activities, f)

    def load_from_file(self, filename='eco_footprint.json'):
        try:
            with open(filename, 'r') as f:
                self.activities = json.load(f)
        except FileNotFoundError:
            print(f"File {filename} not found. Starting fresh.")

# Example Usage
def main():
    tracker = EcoFootprintTracker()
    tracker.load_from_file()

    tracker.add_activity('Driving 10 km', 2.31)
    tracker.add_activity('Eating a beef burger', 2.5)
    tracker.add_activity('Using an LED bulb for 5 hours', 0.08)

    print(f"Total carbon footprint: {tracker.calculate_total_footprint()} kg CO2")
    tracker.visualize_footprint()

    tracker.save_to_file()

if __name__ == '__main__':
    main()