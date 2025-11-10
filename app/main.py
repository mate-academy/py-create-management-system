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
    course: int
    students: list[Student] = dataclasses.field(default_factory=list)


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(group_list, pickle_file)
        max_students = max(len(group.students)
                           for group in group_list) if group_list else 0
        return max_students


def write_students_information(student_list: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(student_list, pickle_file)
    return len(student_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
    speciality_list = set(group.specialty.name for group in groups)
    return speciality_list


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        students_list = pickle.load(pickle_file)
    return students_list
