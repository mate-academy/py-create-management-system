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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(list_of_groups: list[Group]) \
        -> int:
    with open("groups.pickle", "wb") as pfile:
        pickle.dump(list_of_groups, pfile)

    if not list_of_groups:
        return 0

    return max(len(group.students) for group in list_of_groups)


def write_students_information(list_of_students: list[Student]) \
        -> int:
    with open("students.pickle", "wb") as pfile:
        pickle.dump(list_of_students, pfile)
        return len(list_of_students)


def read_groups_information(file_name: str = "groups.pickle") -> set:
    with open(file_name, "rb") as pickle_file:
        groups = pickle.load(pickle_file)
    specialties = {group.specialty.name for group in groups}
    return specialties


def read_students_information(file_name: str = "students.pickle") \
        -> list[Student]:
    with open(file_name, "rb") as pickle_file:
        students = pickle.load(pickle_file)
    return students
