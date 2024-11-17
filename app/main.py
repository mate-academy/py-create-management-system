# write your code here
from datetime import datetime
import pickle
import os
from typing import List, Set
from app.university_classes import Group, Student, Specialty


def write_groups_information(groups: List[Group]) -> int:
    if not groups:
        return []
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> Set[str]:
    if not os.path.isfile("groups.pickle"):
        return {}
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    specialties = {group.specialty.name for group in groups}
    return specialties


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students


# Create some specialties
specialty1 = Specialty(name="Computer Science", number=101)
specialty2 = Specialty(name="Mathematics", number=102)

# Create some students
student1 = Student(
    first_name="John",
    last_name="Doe",
    birth_date=datetime(2000, 1, 1),
    average_mark=4.5,
    has_scholarship=True,
    phone_number="123-456-7890",
    address="123 Main St"
)

student2 = Student(
    first_name="Jane",
    last_name="Smith",
    birth_date=datetime(2001, 2, 2),
    average_mark=3.8,
    has_scholarship=False,
    phone_number="098-765-4321",
    address="456 Elm St"
)

# Create some groups
group1 = Group(specialty=specialty1, course=1, students=[student1, student2])
group2 = Group(specialty=specialty2, course=2, students=[student1])

# Write groups and students information
max_students = write_groups_information([group1, group2])
print(f"Maximum number of students in any group: {max_students}")

num_students = write_students_information([student1, student2])
print(f"Number of students: {num_students}")

# Read groups and students information
specialties = read_groups_information()
print(f"Specialties: {specialties}")

students = read_students_information()
print(f"Students: {students}")
