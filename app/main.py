from dataclasses import dataclass
import datetime
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
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
    max_students = 0

    for group in groups:
        num_students = len(group.students)
        max_students = max(max_students, num_students)

    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    num_students = len(students)
    return num_students


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

    return students


def read_groups_information() -> set:
    specialties = set()

    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
        for group in groups:
            specialties.add(group.specialty.name)

    return specialties
