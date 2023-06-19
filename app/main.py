import dataclasses
from datetime import date
import pickle


@dataclasses.dataclass()
class Specialty:
    name: str
    number: int


@dataclasses.dataclass()
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass()
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    count_st = 0
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    for group in groups:
        count_st = max(count_st, len(group.students))
    return count_st


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    specialty = []
    for group in groups:
        if group.specialty.name not in specialty:
            specialty.append(group.specialty.name)
    return specialty


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
