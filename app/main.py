import pickle
from dataclasses import dataclass


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
        if groups:
            max_students_count = max(len(group.students) for group in groups)
        else:
            max_students_count = 0
    return max_students_count


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list[Specialty]:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    specialities = []
    for group in groups:
        if group.specialty.name in specialities:
            continue
        specialities.append(group.specialty.name)
    return specialities


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
