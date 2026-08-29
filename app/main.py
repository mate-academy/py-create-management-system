import pickle
from datetime import datetime
from dataclasses import dataclass


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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    result = [len(group.students) for group in groups]
    if result:
        return max(result)
    else:
        return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> list:
    unique_specialties = []
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
        for group in groups:
            unique_specialties.append(group.specialty.name)
    return list(set(unique_specialties))


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        student = pickle.load(f)
    return student
