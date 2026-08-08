import pickle
from dataclasses import dataclass
from datetime import date


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as groups_file:
        for group in groups:
            pickle.dump(group, groups_file)
    count_students = 0
    set_student = []
    for group in groups:
        for student in group.students:
            if student not in set_student:
                count_students += 1
                set_student.append(student)
    return count_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        for student in students:
            pickle.dump(student, students_file)
    return len(students)


def read_groups_information() -> list[str]:
    list_groups = []
    with open("groups.pickle", "rb") as groups_file:
        while True:
            try:
                list_groups.append(pickle.load(groups_file))
            except EOFError:
                break
    return list(set([groups.specialty.name for groups in list_groups]))


def read_students_information() -> list[Student]:
    list_students = []
    with open("students.pickle", "rb") as students_file:
        while True:
            try:
                list_students.append(pickle.load(students_file))
            except EOFError:
                break
    return list_students
