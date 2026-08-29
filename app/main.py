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
    birth_date: datetime.date
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
    max_student = 0
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(list_of_groups, pickle_file)
    for group in list_of_groups:
        if len(group.students) > max_student:
            max_student = len(group.students)
    return max_student


def write_students_information(list_of_student: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(list_of_student, pickle_file)
    return len(list_of_student)


def read_groups_information() -> list:
    list_of_specialties = []
    with open("groups.pickle", "rb") as pickle_file:
        list_of_groups: list[Group] = pickle.load(pickle_file)
    for group in list_of_groups:
        list_of_specialties.append(group.specialty.name)
    return list(set(list_of_specialties))


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        return pickle.load(pickle_file)
