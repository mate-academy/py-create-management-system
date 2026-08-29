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


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    max_of_students = 0

    for group in groups:
        if len(group.students) > max_of_students:
            max_of_students = len(group.students)

    return max_of_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> list:
    list_of_specialties = set()
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
        for group in groups:
            list_of_specialties.add(group.specialty.name)
    return list_of_specialties


def read_students_information() -> list:
    list_to_return = []
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
        for student in students:
            list_to_return.append(student)
    return list_to_return
