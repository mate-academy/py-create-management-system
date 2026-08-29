import pickle
import dataclasses
from datetime import datetime


@dataclasses.dataclass
class Specialty:
    name: str
    number: str


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


def write_groups_information(list_of_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(list_of_groups, pickle_file)

    if not list_of_groups:
        return 0

    return max([len(group.students) for group in list_of_groups])


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(list_of_students, pickle_file)

    return len(list_of_students)


def read_groups_information(groups_file: str = "groups.pickle") -> list:
    with open(groups_file, "rb") as pickle_file:
        groups: list[Group] = pickle.load(pickle_file)

    specialties = {group.specialty.name for group in groups}
    return list(specialties)


def read_students_information(students_file: str = "students.pickle") -> list:
    with open(students_file, "rb") as pickle_file:
        students: list[Student] = pickle.load(pickle_file)

    return students
