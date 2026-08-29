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
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:

    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    max_students = 0

    for group in groups:
        num_students = len(group.students)
        if num_students and num_students > max_students:
            max_students = num_students

    return max_students


def write_students_information(students: list[Student]) -> int:

    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> list[str]:

    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

    specialties = []
    for group in groups:
        specialties.append(group.specialty.name)

    return list(set(specialties))


def read_students_information() -> list[Student]:

    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

    return students
