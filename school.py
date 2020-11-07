class School():
    city = 'New York City'

    def __init__(self, dbn, name, boro, writing_score, math_avg, 
            reading_avg, total_students, attendance_rate):
        self.dbn = dbn
        self.name = name
        self.boro = boro
        self.writing_score = writing_score
        self.math_avg = math_avg
        self.reading_avg = reading_avg
        self.total_students = total_students
        self.attendance_rate = attendance_rate

    def total_score(self):
        return self.writing_score + self.math_avg + self.reading_avg

    def avg_student_attendance(self):
        return self.total_students*self.attendance_rate

    def max_score(self):
        scores = [self.writing_score, self.reading_avg, self.math_avg]
        return max(scores)
