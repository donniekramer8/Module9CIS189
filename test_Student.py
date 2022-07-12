"""
Program: test_Student.py
Author: Donnie Kramer
Last date modified: 07/12/2022

The purpose of this program unit test the Student.py file. I don't really understand this. I don't really understand
the point of it either.
"""


import unittest
from class_definitions.Student import Student


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.Me = Student("Kramer", "Donnie", "Biology", "3.91")

    def tearDown(self):
        del self.Me

    def test_object_created_required_attributes(self):
        self.assertEqual(self.Me.last_name, "Kramer")
        self.assertEqual(self.Me.first_name, "Donnie")
        self.assertEqual(self.Me.major, "Biology")
        self.assertEqual(self.Me.gpa, "3.91")

    def test_object_created_all_atributes(self):
        Me = Student("Kramer", "Donnie", "Biology", "3.91")
        assert Me.last_name == "Kramer"
        assert Me.first_name == "Donnie"
        assert Me.major == "Biology"
        assert Me.gpa == "3.91"

    def test_student_str(self):
        self.assertEqual(str(self.Me), "Kramer, Donnie has major Biology with gpa: 3.91")

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            Student("123", "Donnie", "Biology", "3.91")

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            Student("Kramer", "123", "Biology", "3.91")

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            Student("Kramer", "Donnie", "123", "3.91")

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            Student("Kramer", "Donnie", "Biology", "3.91ss")


if __name__ == "__main__":
    unittest.main()
