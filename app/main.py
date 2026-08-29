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
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(list_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        for group in list_groups:
            pickle.dump(group, file)

    if not list_groups:
        return 0
    return max(len(group.students) for group in list_groups)


def write_students_information(list_students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in list_students:
            pickle.dump(student, file)
    return len(list_students)


def read_groups_information() -> list:
    groups = []
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
                groups.append(group)
            except EOFError:
                break

    list_speciality = list(set([group.specialty.name for group in groups]))
    return list_speciality


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                student = pickle.load(file)
                students.append(student)
            except EOFError:
                break

    return students
