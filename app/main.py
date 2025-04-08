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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(group_list, pickle_file)
    if not group_list:
        return 0
    max_number = max(len(group.students) for group in group_list)
    return max_number


def write_students_information(student_list: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(student_list, pickle_file)
    return len(student_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
    return set([group.specialty.name for group in groups])


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        students = pickle.load(pickle_file)
    return students
