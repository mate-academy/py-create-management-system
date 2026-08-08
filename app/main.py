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


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    max_students_in_group = max(
        (len(group.students) for group in groups), default=0
    )
    return max_students_in_group


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information(file_name: str = "groups.pickle") -> list:
    with open(file_name, "rb") as file_name:
        groups = pickle.load(file_name)
        groups_spec = list(set(str(group.specialty.name) for group in groups))
    return groups_spec


def read_students_information(file_name: str = "students.pickle") -> list:
    with open(file_name, "rb") as file_name:
        students = pickle.load(file_name)
        students_list = students
    return students_list
