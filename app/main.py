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
    course: str
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(group_list, file)

    number_students = [len(group.students) for group in group_list]
    return max(number_students) if number_students else 0


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students_list, file)

    return len(students_list)


def read_groups_information(file_name: str = "groups.pickle") -> set:
    with open(file_name, "rb") as file:
        groups = pickle.load(file)

    specialties_groups = set(group.specialty.name for group in groups)
    return specialties_groups


def read_students_information(file_name: str = "students.pickle") -> list:
    with open(file_name, "rb") as file:
        students_list = pickle.load(file)
    return students_list
