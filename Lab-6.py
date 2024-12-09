import pickle

class Course_grades:
    def __init__(self, course_name, stu_ID, stu_grade):
        self.course_name = course_name
        self.stu_ID = stu_ID
        self.stu_grade = stu_grade

    def __str__(self):
        return (f"Course: {self.course_name}\n"
                f"Student IDs: {self.stu_ID}\n"
                f"Grades: {self.stu_grade}\n")

courses = []
for i in range(4):
    course_name = input(f"Enter course name for course {i + 1}: ")
    stu_ID = [input(f"Enter Student ID {j + 1}: ") for j in range(5)]
    stu_grade = [int(input(f"Enter grade for Student {j + 1} (0-100): ")) for j in range(5)]
    courses.append(Course_grades(course_name, stu_ID, stu_grade))

with open("grades_info.dat", "ab") as file:
    for course in courses:
        pickle.dump(course, file)

print("\nReading objects from the file...\n")
read_courses = []
with open("grades_info.dat", "rb") as file:
    while True:
        try:
            read_courses.append(pickle.load(file))
        except EOFError:
            break

for i, course in enumerate(read_courses, start=1):
    print(f"Course {i} Information:")
    print(course)
    print("-" * 40)
