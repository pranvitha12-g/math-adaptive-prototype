class AdaptiveEngine:
    def __init__(self):
        self.difficulty_levels = ['Easy', 'Medium', 'Hard']
        self.current_level = 'Medium'
        self.correct_streak = 0
        self.incorrect_streak = 0

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
