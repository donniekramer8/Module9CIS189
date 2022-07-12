"""
Program: Student.py
Author: Donnie Kramer
Last date modified: 07/12/2022

The purpose of this program is to create an object that stores some variables. Then I will test it in the test_Student
file.
"""


class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=''):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        gpa_characters = set("1234567890.")
        if not name_characters.issuperset(lname) or not name_characters.issuperset(
                fname) or not name_characters.issuperset(major):
            raise ValueError
        if gpa and not gpa_characters.issuperset(gpa):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return f"{self.last_name}, {self.first_name} has major {self.major} with gpa: {str(self.gpa)}"


if __name__ == "__main__":
    a = Student("Kramer", "Donnie", "Biology", "3.91")
    print(a)
    del a
