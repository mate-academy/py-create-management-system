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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set[str]:
    with open("groups.pickle", "rb") as pickle_file:
        user_1 = pickle.load(pickle_file)
        specialties = [group.specialty.name for group in user_1]
        return set(specialties)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        user_1 = pickle.load(pickle_file)
        return user_1
