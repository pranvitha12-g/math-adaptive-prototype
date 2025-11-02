import time

class PerformanceTracker:
    def __init__(self):
        self.records = []

    def record(self, correct, duration, level):
        self.records.append({'correct': correct, 'time': duration, 'level': level})

    def summary(self):
        total = len(self.records)
        correct = sum(r['correct'] for r in self.records)
        avg_time = sum(r['time'] for r in self.records) / total if total else 0
        accuracy = (correct / total * 100) if total else 0
        return {'total': total, 'accuracy': accuracy, 'avg_time': round(avg_time, 2)}
