from oopconcepts.college import College

class Student(College):
    def __init__(self, cname, ccode, ccity, rollno, sname, mark1, mark2, mark3):
        super().__init__(cname, ccode, ccity)
        self.rollno = rollno
        self.sname = sname
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calculate_total(self):
        return self.mark1 + self.mark2 + self.mark3

    def calculate_average(self):
        return self.calculate_total()/3