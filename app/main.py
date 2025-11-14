import pickle
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Specialty():
    name: str
    number: int


@dataclass
class Student():
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group():
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_of_students: list[Group]) -> int:
    max_students = max((len(group.students)
                        for group in group_of_students), default=0)
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(group_of_students, pickle_file)
    return max_students


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(list_of_students, pickle_file)
    return len(list_of_students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as pickle_file:
        groups_list: list[Group] = pickle.load(pickle_file)
    specialties = {group.specialty.name for group in groups_list}
    return list(specialties)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        students_list: list[Student] = pickle.load(pickle_file)
    return students_list
