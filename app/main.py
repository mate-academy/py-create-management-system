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


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(groups, groups_file)
    count_students = []
    for group in groups:
        count_students.append(len(group.students))
    if count_students:
        return max(count_students)
    else:
        return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students, students_file)
    return len(students)


def read_groups_information() -> set[str]:
    with open("groups.pickle", "rb") as groups_file:
        groups = pickle.load(groups_file)
    specialty_list = []
    for group in groups:
        specialty_list.append(group.specialty.name)
    return set(specialty_list)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as students_file:
        return pickle.load(students_file)
