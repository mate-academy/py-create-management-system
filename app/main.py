import dataclasses
import pickle
from datetime import datetime


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)
    return len(students)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        students_list = []
        while True:
            try:
                student = pickle.load(f)
            except EOFError:
                break
            else:
                students_list.append(student)
    return students_list


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        max_students = 0
        for group in groups:
            if len(group.students) > max_students:
                max_students = len(group.students)
            pickle.dump(group, f)
    return max_students


def read_groups_information() -> set[str]:
    with open("groups.pickle", "rb") as f:
        groups_set = set()
        while True:
            try:
                group = pickle.load(f)
            except EOFError:
                break
            else:
                groups_set.add(group.specialty.name)
    return groups_set
