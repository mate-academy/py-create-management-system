from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass
class Specialty:
    name: str
    number: str


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
    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(groups, groups_file)
    if not groups:
        return 0
    total_students = max(len(group.students) for group in groups)
    return total_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students, students_file)
    return len(students)


def read_groups_information(output_file: str = "groups.pickle") -> list:
    with open(output_file, "rb") as groups_pickle:
        groups = pickle.load(groups_pickle)
    specialties = set(group.specialty.name for group in groups)
    return list(specialties)


def read_students_information(output_file: str = "students.pickle") -> list:
    with open(output_file, "rb") as students_pickle:
        students = list(pickle.load(students_pickle))
    return students
