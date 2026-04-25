from oopconcepts.student import Student

class StudentGrade(Student):
    def __init__(self, cname, ccode, ccity, rollno, sname, mark1, mark2, mark3):
        super().__init__(cname, ccode, ccity, rollno, sname, mark1, mark2, mark3)
        self.result = 0
        self.grade = 'None'

    def calculate_result(self):
        if self.mark1 >= 40 and self.mark2 >= 40 and self.mark3 >= 40:
            self.result = 'Pass'
        else:
            self.result = 'Fail'

    def calculate_grade(self):
        if self.result == 'Pass':
            if super().calculate_average() >= 80:
                self.grade = 'A'
            elif super().calculate_average() >= 70:
                self.grade = 'B'
            elif super().calculate_average() >= 60:
                self.grade = 'C'
            elif super().calculate_average() >= 50:
                self.grade = 'D'
            elif super().calculate_average() >= 40:
                self.grade = 'E'
            else:
                self.grade = 'NA'