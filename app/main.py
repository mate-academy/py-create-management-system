import dataclasses
import pickle
from datetime import datetime


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
    course: list
    students: list[Student]


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            pickle.dump(group, pickle_file)
    max_value = 0
    if groups:
        print(groups)
        max_value = max([len(group.students) for group in groups])
    return max_value


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
    return len(students)


def read_groups_information() -> list:
    specialties_names = []
    with open("groups.pickle", "rb") as pickle_file:
        try:
            while True:
                group = pickle.load(pickle_file)
                if group.specialty.name not in specialties_names:
                    specialties_names.append(group.specialty.name)
        except EOFError:
            return specialties_names


def read_students_information() -> list:
    students_list = []
    with open("students.pickle", "rb") as pickle_file:
        try:
            while True:
                student = pickle.load(pickle_file)
                students_list.append(student)
        except EOFError:
            return students_list
