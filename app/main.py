from dataclasses import dataclass
from datetime import datetime
import pickle


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


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def write_groups_information(groups: list[Group]) -> int:
    students_count = []
    for group in groups:
        students_count.append(len(group.students))

    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    if students_count == []:
        return 0
    return max(students_count)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    if groups == []:
        return []

    spetialties = set()
    for group in groups:
        spetialties.add(group.specialty.name)

    return list(spetialties)
