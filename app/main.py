from datetime import datetime
import pickle
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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_students = max(len(group.students)
                       for group in groups) if groups else 0

    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> set[Group]:
    try:
        with open("groups.pickle", "rb") as file_obj:
            groups = pickle.load(file_obj)
    except FileNotFoundError:
        return set()

    # extraction of unique speciality names
    speciality_names = {group.specialty.name for group in groups}
    return speciality_names


def read_students_information() -> list[Student]:
    try:
        with open("students.pickle", "rb") as file_obj:
            students = pickle.load(file_obj)
    except FileNotFoundError:
        return list()

    return students
