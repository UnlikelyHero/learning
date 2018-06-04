class LotteryPlayer:
    def __init__(self, name, numbers):
        self.name = name,
        self.numbers = numbers

    def total(self):
        return sum(self.numbers)


Rolf = LotteryPlayer("Rolf", (5, 9, 12, 3, 1, 21)),
John = LotteryPlayer("John", (6, 10, 13, 4, 2, 22)),
Don = LotteryPlayer("Don", (7, 11, 14, 5, 3, 23)),


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def go_to_school(cls):
        print("I'm going to school.")
        print("I'm a {}".format(cls))


anna = Student("Anna", "MIT")
rolf = Student("Rolf", "Oxford")
anna.marks.append(56)
anna.marks.append(71)
anna.go_to_school()
