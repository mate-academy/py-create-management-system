import pickle
import dataclasses
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
    course: int | datetime
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:

    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    max_students_in_group = 0
    for group in groups:
        if len(group.students) > max_students_in_group:
            max_students_in_group = len(group.students)

    return max_students_in_group


def write_students_information(students: list[Student]) -> int:

    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> list:

    with open("groups.pickle", "rb") as f:
        data = pickle.load(f)
        all_specialties = []
    for group in data:
        if group.specialty.name not in all_specialties:
            all_specialties.append(group.specialty.name)

    return all_specialties


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        data = pickle.load(f)
    return [
        student for student in data if isinstance(student, Student)
    ]
