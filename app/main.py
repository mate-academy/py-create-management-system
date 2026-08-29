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
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    students_group = []
    for group in groups:
        students_group.append(len(group.students))
    if len(students_group) > 0:
        return max(students_group)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information(groups_file: str = "groups.pickle") -> set:
    with open(groups_file, "rb") as f:
        groups = pickle.load(f)
    result = set()
    for group in groups:
        result.add(group.specialty.name)
    return result


def read_students_information(students_file: str = "students.pickle") -> list:
    with open(students_file, "rb") as f:
        students_list = pickle.load(f)
    return students_list
