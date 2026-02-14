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


def write_groups_information(group_list: list[Group]) -> int:
    total_students = []
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(group_list, pickle_file)
    for group in group_list:
        total_students.append(len(group.students))
    max_count = max(total_students) if len(total_students) > 0 else 0
    return max_count


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information() -> list:
    specialties_list = []
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)

    for group in groups:
        if group.specialty.name not in specialties_list:
            specialties_list.append(group.specialty.name)

    return specialties_list


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        students_list = pickle.load(pickle_file)
    return students_list
