class Student:

    def __init__(self, fullname, gender, birth_year):
        self.fullname = fullname
        self.gender = gender
        self.birth_year = birth_year

    def __str__(self):
        return f'{self.fullname} {self.gender} {self.birth_year}'
