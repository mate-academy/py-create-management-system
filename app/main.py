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
    phone_number: str
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
        return max(len(group.students) for group in groups)
    return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> list[str]:
    try:
        with open("groups.pickle", "rb") as file:
            groups = pickle.load(file)
            specialties = {group.specialty.name for group in groups}
            return list(specialties)
    except FileNotFoundError:
        print("File groups.pickle not found.")
        return []


def read_students_information() -> list[Student]:
    try:
        with open("students.pickle", "rb") as file:
            students = pickle.load(file)
            return students
    except FileNotFoundError:
        print("File students.pickle not found.")
        return []
