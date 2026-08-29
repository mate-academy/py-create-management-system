import pickle
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as groups_file:
        for group in groups:
            pickle.dump(group, groups_file)
            if len(group.students) > max_students:
                max_students = len(group.students)
    return max_students


def write_students_information(students: list[Student]) -> int:
    students_count = 0
    with open("students.pickle", "wb") as students_file:
        for student in students:
            pickle.dump(student, students_file)
            students_count += 1
    return students_count


def read_groups_information() -> set:
    result = []
    groups_file = open("groups.pickle", "rb")
    while 1:
        try:
            result.append(pickle.load(groups_file))
        except EOFError:
            break
    groups_file.close()
    return set([group.specialty.name for group in result])


def read_students_information() -> list[Student]:
    result = []
    students_file = open("students.pickle", "rb")
    while 1:
        try:
            result.append(pickle.load(students_file))
        except EOFError:
            break
    students_file.close()
    return result
