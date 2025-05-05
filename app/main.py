import dataclasses
import pickle

from datetime import datetime


@dataclasses.dataclass()
class Specialty:
    name: str
    number: int


@dataclasses.dataclass()
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass()
class Group:
    specialty: Specialty
    course: int | datetime
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_students = 0

    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            if len(group.students) > max_students:
                max_students = len(group.students)
            pickle.dump(group, pickle_file)

    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)

    return len(students)


def read_groups_information() -> set:
    specialties_names = set()
    groups = []

    try:
        with open("groups.pickle", "rb") as pickle_file:
            while True:
                groups.append(pickle.load(pickle_file))
    except EOFError:
        pass

    for group in groups:
        specialties_names.add(group.specialty.name)

    return specialties_names


def read_students_information() -> list:
    students = []
    try:
        with open("students.pickle", "rb") as pickle_file:
            while True:
                students.append(pickle.load(pickle_file))
    except EOFError:
        pass

    return [student for student in students]
