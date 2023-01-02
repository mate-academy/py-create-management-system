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
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as group_file:
        pickle.dump(groups, group_file)

    max_students = 0

    for group in groups:
        if len(group.students) > max_students:
            max_students = len(group.students)

    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as student_file:
        pickle.dump(students, student_file)

    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as group_file:
        group_list = pickle.load(group_file)

    return set(group.specialty.name for group in group_list)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as group_file:
        students_list = pickle.load(group_file)

    return students_list
