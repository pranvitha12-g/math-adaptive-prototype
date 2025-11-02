from puzzle_maker import generate_puzzle
from performance_tracker import PerformanceTracker
from adaptive_logic import AdaptiveEngine
import time

def main():
    print("=== Math Adventures: Adaptive Learning Prototype ===")
    name = input("Enter your name: ")
    engine = AdaptiveEngine()
    tracker = PerformanceTracker()

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

if __name__ == "__main__":
    main()
