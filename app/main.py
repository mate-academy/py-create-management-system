import dataclasses
from datetime import datetime
import pickle


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
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)

    max_students_number = 0
    for group in groups:
        if len(group.students) > max_students_number:
            max_students_number = len(group.students)
    return max_students_number


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)

    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
        specialties = set()
        for group in groups:
            specialties.add(group.specialty.name)
        return list(specialties)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        return pickle.load(pickle_file)
