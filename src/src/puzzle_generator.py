Directory: src/

Files: main.py, puzzle_generator.py, tracker.py, adaptive_engine.py

--- puzzle_generator.py ---

import random

def generate_puzzle(level): if level == 'Easy': a, b = random.randint(1, 10), random.randint(1, 10) op = random.choice(['+', '-']) elif level == 'Medium': a, b = random.randint(10, 50), random.randint(1, 20) op = random.choice(['+', '-', '']) else:  # Hard a, b = random.randint(20, 100), random.randint(2, 10) op = random.choice(['', '/'])

question = f"{a} {op} {b}"
try:
    answer = eval(question)
except ZeroDivisionError:
    return generate_puzzle(level)
return question, round(answer, 2)

--- tracker.py ---

import time

class PerformanceTracker: def init(self): self.records = []

def record(self, correct, duration, level):
    self.records.append({'correct': correct, 'time': duration, 'level': level})

def summary(self):
    total = len(self.records)
    correct = sum(r['correct'] for r in self.records)
    avg_time = sum(r['time'] for r in self.records) / total if total else 0
    accuracy = (correct / total * 100) if total else 0
    return {'total': total, 'accuracy': accuracy, 'avg_time': round(avg_time, 2)}

--- adaptive_engine.py ---

class AdaptiveEngine: def init(self): self.difficulty_levels = ['Easy', 'Medium', 'Hard'] self.current_level = 'Medium' self.correct_streak = 0 self.incorrect_streak = 0

def update_difficulty(self, correct, response_time):
    if correct and response_time < 10:
        self.correct_streak += 1
        self.incorrect_streak = 0
    else:
        self.incorrect_streak += 1
        self.correct_streak = 0

    idx = self.difficulty_levels.index(self.current_level)

    if self.correct_streak >= 3 and idx < 2:
        self.current_level = self.difficulty_levels[idx + 1]
        self.correct_streak = 0
    elif self.incorrect_streak >= 2 and idx > 0:
        self.current_level = self.difficulty_levels[idx - 1]
        self.incorrect_streak = 0

    return self.current_level

--- main.py ---

from puzzle_generator import generate_puzzle from tracker import PerformanceTracker from adaptive_engine import AdaptiveEngine import time

def main(): print("=== Math Adventures: Adaptive Learning Prototype ===") name = input("Enter your name: ") engine = AdaptiveEngine() tracker = PerformanceTracker()

for i in range(5):  # ask 5 questions per session
    level = engine.current_level
    question, answer = generate_puzzle(level)
    print(f"\nLevel: {level} | Question {i+1}: {question}")

    start = time.time()
    try:
        user_answer = float(input("Your Answer: "))
    except ValueError:
        user_answer = None
    end = time.time()

    correct = abs((user_answer or 0) - answer) < 0.01
    duration = end - start
    tracker.record(correct, duration, level)

    if correct:
        print(f"✅ Correct! ({round(duration,2)}s)")
    else:
        print(f"❌ Wrong. Correct answer: {answer} ({round(duration,2)}s)")

    new_level = engine.update_difficulty(correct, duration)
    print(f"Next Level: {new_level}")

print("\n=== Session Summary ===")
summary = tracker.summary()
print(f"Accuracy: {summary['accuracy']}%")
print(f"Average Time: {summary['avg_time']}s")
print(f"Next Recommended Level: {engine.current_level}")

if name == "main": main()
