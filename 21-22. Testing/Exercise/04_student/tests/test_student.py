from project.student import Student
from unittest import TestCase, main


class StudentTest(TestCase):
    # Student inputs
    name = "Ханко Брат"
    courses = {
        "Дървен философизъм": [":P"],
        "DJ-ism": [":S", ":N"],
        "Cooking": [":0"]
    }

    def setUp(self):
        self.student = Student(self.name, self.courses)

    def test_init(self):
        self.assertEqual(self.name, self.student.name)
        self.assertEqual(self.courses, self.student.courses)
        self.assertEqual([_ for _ in self.courses.values()], [_ for _ in self.student.courses.values()])

    def test_init_no_courses(self):
        student = Student(self.name)
        self.assertEqual({}, student.courses)
        self.assertIsInstance(self.student.courses, dict)

    def test_init_types(self):
        self.assertIsInstance(self.student.name, str)
        self.assertIsInstance(self.student.courses, dict)
        self.assertIsInstance(self.student.courses["DJ-ism"], list)

        student = Student(self.name)
        self.assertIsInstance(student.name, str)
        self.assertIsInstance(student.courses, dict)

    def test_enroll_add_notes_to_existing_course(self):
        new_notes = ["New note 1", "New note 2"]
        course = "DJ-ism"
        expected_courses = self.courses.copy()
        [expected_courses[course].append(note) for note in new_notes]
        expected_notes = self.courses[course] + new_notes
        result = self.student.enroll(course, new_notes)

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(expected_courses, self.student.courses)
        self.assertEqual(expected_courses[course], self.student.courses[course])

    def test_enroll_new_course_with_notes(self):
        course = "New Course with notes"
        notes = ["New course note 1", "New course note 2"]
        expected_courses = self.courses.copy()
        expected_courses[course] = notes
        result = self.student.enroll(course, notes)

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(expected_courses, self.student.courses)
        self.assertEqual(expected_courses[course], self.student.courses[course])

    def test_enroll_new_course_with_notes_Y(self):
        course = "Another new Course with notes"
        notes = ["New course note 5", "New course note 4"]
        expected_courses = self.courses.copy()
        expected_courses[course] = notes
        result = self.student.enroll(course, notes, "Y")

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(expected_courses, self.student.courses)
        self.assertEqual(expected_courses[course], self.student.courses[course])

    def test_enroll_new_course_no_notes(self):
        course = "New Course without notes"
        expected_courses = self.courses.copy()
        expected_courses[course] = []
        result = self.student.enroll(course, "", "NO!")

        self.assertEqual("Course has been added.", result)
        self.assertEqual(expected_courses, self.student.courses)
        self.assertEqual(expected_courses[course], self.student.courses[course])

    def test_add_notes(self):
        course = "DJ-ism"
        new_notes = "New note 3"
        expected_courses = self.courses.copy()
        expected_courses[course].append(new_notes)
        expected_notes = self.courses[course] + [new_notes]
        result = self.student.add_notes(course, new_notes)

        self.assertEqual("Notes have been updated", result)
        self.assertEqual(expected_courses, self.student.courses)
        self.assertEqual(expected_notes, self.student.courses[course])

    def test_add_notes_nonexistent_course_exception(self):
        course = "I don't exist"
        new_notes = "Can you find me a home?"
        with self.assertRaises(Exception) as ex:
            self.student.add_notes(course, new_notes)

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course(self):
        course = "DJ-ism"
        expected_courses = self.student.courses.copy()
        expected_courses.pop(course)
        result = self.student.leave_course(course)

        self.assertEqual("Course has been removed", result)
        self.assertEqual(expected_courses, self.student.courses)

    def test_leave_course_nonexistent_course_exception(self):
        course = "DJ-ism"
        with self.assertRaises(Exception) as ex:
            self.student.leave_course(course)

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
