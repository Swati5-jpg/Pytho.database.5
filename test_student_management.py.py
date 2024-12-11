import unittest
from student_management import StudentManagement, Student


class TestStudentManagement(unittest.TestCase):

    def setUp(self):
        """Set up a fresh instance of StudentManagement for each test."""
        self.management = StudentManagement()
        self.management.students = []  # Clear default data for isolated testing

    def test_add_student(self):
        """Test the add_student() method."""
        student = Student(101, "John Doe", 20, "A", ["Math", "Science"])
        self.management.add_student(student)

        # Assertions
        self.assertEqual(len(self.management.students), 1)
        self.assertEqual(self.management.students[0].student_id, 101)
        self.assertEqual(self.management.students[0].name, "John Doe")

    def test_view_students(self):
        """Test the view_students() method."""
        # Add mock students
        student1 = Student(101, "John Doe", 20, "A", ["Math", "Science"])
        student2 = Student(102, "Jane Doe", 22, "B", ["English", "History"])
        self.management.students.extend([student1, student2])

        # Get result
        result = self.management.view_students()
        expected = [
            "ID: 101, Name: John Doe, Age: 20, Grade: A, Subjects: Math, Science",
            "ID: 102, Name: Jane Doe, Age: 22, Grade: B, Subjects: English, History",
        ]

        self.assertEqual(result, expected)

    def test_update_student(self):
        """Test the update_student() method."""
        student = Student(101, "John Doe", 20, "A", ["Math", "Science"])
        self.management.students.append(student)

        # Update the student's name
        self.management.update_student(101, name="John Smith")
        self.assertEqual(self.management.students[0].name, "John Smith")

        # Update the student's grade
        self.management.update_student(101, grade="A+")
        self.assertEqual(self.management.students[0].grade, "A+")

    def test_delete_student(self):
        """Test the delete_student() method."""
        student1 = Student(101, "John Doe", 20, "A", ["Math", "Science"])
        student2 = Student(102, "Jane Doe", 22, "B", ["English", "History"])
        self.management.students.extend([student1, student2])

        # Delete a student by ID
        self.management.delete_student(101)
        self.assertEqual(len(self.management.students), 1)
        self.assertEqual(self.management.students[0].student_id, 102)

    def test_save_students_to_file(self):
        """Test the save_students_to_file() method."""
        student1 = Student(101, "John Doe", 20, "A", ["Math", "Science"])
        student2 = Student(102, "Jane Doe", 22, "B", ["English", "History"])
        self.management.students.extend([student1, student2])

        # Save to file
        self.management.save_students_to_file("test_students.txt")

        # Read the file and validate content
        with open("test_students.txt", "r") as file:
            content = file.read()
            expected = (
                "ID: 101, Name: John Doe, Age: 20, Grade: A, Subjects: Math, Science\n"
                "ID: 102, Name: Jane Doe, Age: 22, Grade: B, Subjects: English, History\n"
            )
            self.assertEqual(content, expected)

    def tearDown(self):
        """Clean up after each test."""
        self.management.students = []
        # Optionally remove the test file
        import os
        if os.path.exists("test_students.txt"):
            os.remove("test_students.txt")


if __name__ == "__main__":
    unittest.main()
