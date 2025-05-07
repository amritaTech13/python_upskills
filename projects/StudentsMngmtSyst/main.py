
class Students:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = {}

    def add_marks(self, subject, score):
        self.marks[subject] = score
    def get_avg(self):
       if self.marks:
          if not self.marks:
              return 0
          else:
            return sum(self.marks.values()) /len(self.marks)

    def get_report(self):
        print("---Report Card---")
        print(f"Student: {self.name}")
        print(f"Roll number: {self.roll_no}")
        print("Marks-")
        for subject, score in self.marks.items():
           print(f"{subject}: {score}")
        print(f"Average: {self.get_avg(): .2f}")   

std1 = Students("Amrita", 101)
std1.add_marks('Hindi', 100)
std1.add_marks('English', 70)
std1.add_marks('Physics', 60)
std1.add_marks('science', 70)
std1.add_marks('Maths', 100)
std1.get_report()

