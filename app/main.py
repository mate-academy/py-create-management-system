import dataclasses
import pickle
from typing import List


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: int
    average_mark: float
    has_scholarship: bool
    phone_number: float
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    maximum_students = 0
    with open("groups.pickle", "wb") as group_file:
        for group in groups:
            pickle.dump(group, group_file)
            maximum_students = max(maximum_students, len(group.students))
    return maximum_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as student_file:
        for student in students:
            pickle.dump(student, student_file)
    return len(students)


def read_groups_information() -> set:
    specialties = set()
    try:
        with open("groups.pickle", "rb") as f:
            while True:
                try:
                    group = pickle.load(f)
                    specialties.add(group.specialty.name)
                except EOFError:
                    break
    except FileNotFoundError:
        print("File 'groups.pickle' not found.")
    return specialties


def read_students_information() -> List[Student]:
    students = []
    try:
        with open("students.pickle", "rb") as f:
            while True:
                try:
                    student = pickle.load(f)
                    students.append(student)
                except EOFError:
                    break
    except FileNotFoundError:
        print("File 'students.pickle' not found.")
    return students

