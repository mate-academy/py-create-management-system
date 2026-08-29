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
    course: int
    students: list[Student]


def write_groups_information(list_of_groups: list[Group]) -> int:
    max_students = 0
    if len(list_of_groups) != 0:
        max_students = max(len(g.students) for g in list_of_groups)
    with open("groups.pickle", "wb") as f:
        pickle.dump(list_of_groups, f)
    return max_students


def write_students_information(list_of_students: list[Student]) -> int:
    amount_of_students = len(list_of_students)
    with open("students.pickle", "wb") as f:
        pickle.dump(list_of_students, f)
    return amount_of_students


def read_groups_information() -> list[str]:
    list_of_groups = []
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
        for group in groups:
            if group.specialty.name not in list_of_groups:
                list_of_groups.append(group.specialty.name)
    return list_of_groups


def read_students_information() -> list[Student]:
    list_of_students = []
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
        for student in students:
            list_of_students.append(student)
    return list_of_students
