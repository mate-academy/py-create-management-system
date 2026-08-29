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
    if len(groups) > 0:
        total = max(len(group.students) for group in groups)
    else:
        return 0

    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    return total


def write_students_information(students: list[Student]) -> int:
    total = len(students)
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return total


def read_groups_information() -> set[str] | list:
    original_speciality = []
    try:
        with open("groups.pickle", "rb") as file:
            obj = pickle.load(file)
            for group in obj:
                original_speciality.append(group.specialty.name)
    except FileNotFoundError:
        return original_speciality

    return set(original_speciality)


def read_students_information() -> list[Student]:
    full_list = []
    with open("students.pickle", "rb") as file:
        obj = pickle.load(file)
        for student in obj:
            full_list.append(student)

    return full_list
