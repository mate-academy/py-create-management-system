import dataclasses
from datetime import datetime
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        max_students = 0
        for group in groups:
            pickle.dump(group, pickle_file)
            max_students = max(max_students, len(group.students))
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as pickle_file:
        group_set = set()
        while True:
            try:
                group = pickle.load(pickle_file)
                group_set.add(group.specialty.name)
            except EOFError:
                break
    return group_set


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        students = []
        while True:
            try:
                student = pickle.load(pickle_file)
                students.append(student)
            except EOFError:
                break
    return students
