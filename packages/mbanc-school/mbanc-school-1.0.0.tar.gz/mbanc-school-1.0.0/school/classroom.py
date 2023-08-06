from school.student import Student


class Classroom:

    def __init__(self, year_of_creation, classroom_char, students):
        self.year_of_creation = year_of_creation
        self.classroom_char = classroom_char
        self.students = students

    def show_student(self):
        for student in self.students:
            print(student)
        return

    def add_student(self, student):
        self.students.append(student)


if __name__ == '__main__':
    students = [
        Student('Grzegorz Brzeczyszczykiewicz', 'M', 1950),
        Student('Donald Trump', 'M', 1900),
        Student('Angela Merkel', 'F', 1900),
    ]

    classroom1 = Classroom(
        year_of_creation=2021,
        classroom_char='A',
        students=students,
    )
    classroom1.show_student()

    classroom2 = Classroom(
        year_of_creation=1990,
        classroom_char='B',
        students=[
            Student('Agelina Jolie', 'F', 1980),
        ],
    )
    classroom2.show_student()
    classroom2.add_student(student=Student('Patryk Wiener', 'M', 1997))
