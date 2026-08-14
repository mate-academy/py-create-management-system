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
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)

    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)

    return len(students)


def read_groups_information() -> list[str]:
    specialties = set()

    with open("groups.pickle", "rb") as f:
        try:
            while True:
                obj = pickle.load(f)
                if isinstance(obj, list):
                    for group in obj:
                        specialties.add(group.specialty.name)
                else:
                    specialties.add(obj.specialty.name)
        except EOFError:
            pass

    return list(specialties)


def read_students_information() -> list[Student]:
    students = []

    with open("students.pickle", "rb") as f:
        try:
            while True:
                obj = pickle.load(f)
                if isinstance(obj, list):
                    students.extend(obj)
                else:
                    students.append(obj)
        except EOFError:
            pass

    return students
