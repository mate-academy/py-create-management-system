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
    average_mark: int
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int | list:
    with open("groups.pickle", "wb") as f:
        pickle.dump(group_list, f)
    if not group_list:
        return []
    return max([len(group.students) for group in group_list])


def write_students_information(student_list: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(student_list, f)
    return len(student_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        data_groups = pickle.load(f)
    names = [data.specialty.name for data in data_groups]
    return set(names)


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        data_students = pickle.load(f)
    return [student for student in data_students]
