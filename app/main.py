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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int | datetime
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
    result_name = []
    if not groups:
        return []
    for group in groups:
        result_name.append(group.specialty.name)

    return sorted(list(set(result_name)))


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        students = pickle.load(pickle_file)
    result = []
    if not students:
        return []
    for student in students:
        result.append(student)

    return result
