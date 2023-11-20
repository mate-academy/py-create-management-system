# write your code here
import dataclasses
import pickle
from builtins import int
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
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    group_list = [len(group.students) for group in groups]
    return max(group_list) if len(group_list) > 0 else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        specialties = set(group.specialty.name for group in pickle.load(file))
        return list(specialties)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        return [student for student in pickle.load(file)]
