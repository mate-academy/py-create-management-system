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
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_group = 0
    with open("groups.pickle", "wb") as file:
        for group in groups:
            max_group = max(max_group, len(group.students))
            pickle.dump(group, file)
    return max_group


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information() -> list[Group]:
    spec_names = []
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                spec_names.append(pickle.load(file).specialty.name)
            except EOFError:
                break
    return list(set(spec_names))


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                students.append(pickle.load(file))
            except EOFError:
                break
    return students
