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
    students: list[Student]


def write_groups_information(ls_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as fil:
        pickle.dump(ls_groups, fil)
    if not ls_groups:
        return 0
    return max(len(student.students) for student in ls_groups)


def write_students_information(ls_students: list[Student]) -> int:
    with open("students.pickle", "wb") as fil:
        pickle.dump(ls_students, fil)
    return len(ls_students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as fil:
        data_groups = pickle.load(fil)
    return list(set(group.specialty.name for group in data_groups))


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as fil:
        data_students = pickle.load(fil)
        return data_students
