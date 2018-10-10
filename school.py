class School:
    def __init__(self, name):
        self.name = name
        self._roster = {}

    def roster(self):
        return self._roster

    def add_student(self, student, grade):
        if grade in self._roster:
            self._roster[grade].append(student)
        else:
            self._roster[grade] = [student]
        return self._roster

    def grade(self, grade):
        return self._roster[grade]

    def sort_roster(self):
        return [(k, self._roster[k]) for k in sorted(self._roster, key=self._roster.get)]
