import dataclasses
from datetime import datetime
import pickle


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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(list_group: list[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as pickle_file:
        for group in list_group:
            pickle.dump(group, pickle_file)
            max_students = max(max_students, len(group.students))
    return max_students


def write_students_information(list_students: list[Student]) -> int:
    number_students = 0
    with open("students.pickle", "wb") as pickle_file:
        for student in list_students:
            pickle.dump(student, pickle_file)
            number_students += 1
    return number_students


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_file:
        groups = []
        while True:
            try:
                group = pickle.load(pickle_file)
                if group.specialty.name not in groups:
                    groups.append(group.specialty.name)
            except EOFError:
                break
    return groups


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        students = []
        while True:
            try:
                student = pickle.load(pickle_file)
                students.append(student)
            except EOFError:
                break
        return students
