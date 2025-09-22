 #Create tuples to store student information (name, age, grade).

student1 = ('Ali', 20, 'C') # name, age, grade
student2=("Yousef", 34, "A")
student3=("Kamran", 30, "B")

print(student1)

# Create a tuple of students records
students = (student1, student2, student3)

#use tuple methods
print(f"Number of student: {len(students)}")
print(f"Index of Kamran: {students.index(student3)}\n")

#============2 Create sets for student IDs and courses
student_ids = {101, 102, 103} #unique ids
print(f"Student IDs: {student_ids}")

#add new student
new_student = {104, 105}
student_ids.update(new_student)
print(f"Updated Student IDs: {student_ids}\n")

#students courses
courses_student1 = {"Math", "Physics", "Chemistry"}
courses_student2 = {"Biology", "Math", "Chemistry"}
courses_student3 = {"Math", "History", "Sience"}

print(f"Courses Student1: {courses_student1}")
print(f"Courses Student2: {courses_student2}")
print(f"Courses Student3: {courses_student3}\n")

#all courses without repetition .union
all_courses = courses_student1.union(courses_student2).union(courses_student3)
print (f"All courses:  {all_courses}")

#Common_courses between two students .intersection
common_courses = courses_student1.intersection(courses_student2)
print(f"Common courses between Student1 & Student2: {common_courses}")

#unique courses for student1
unique_courses_student1 = courses_student1.difference(courses_student2)
print("Courses only student1 has: {unique_courses_student1}\n")


#========3 frozen set (immutable)
frozen_courses = frozenset(all_courses)
print(f"Frozen Courses: {frozen_courses}")

frozen_student_data = frozenset(students)
print(f"Frozen Student Data: {frozen_student_data}")