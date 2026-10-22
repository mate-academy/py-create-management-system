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


def write_groups_information(groups_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups_list, file)
    if not groups_list:
        return 0
    max_students = max(len(group.students) for group in groups_list)
    return max_students


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students_list, file)
    return len(students_list)


def read_groups_information() -> list[str]:
    try:
        with open("groups.pickle", "rb") as file:
            groups_list = pickle.load(file)
        specialties_names = set(group.specialty.name for group in groups_list)
        return list(specialties_names)
    except FileNotFoundError:
        return []


def read_students_information() -> list[Student]:
    try:
        with open("students.pickle", "rb") as file:
            students_list = pickle.load(file)
        return students_list
    except FileNotFoundError:
        return []
