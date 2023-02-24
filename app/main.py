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


def write_groups_information(ls: list[Group]) -> int:
    with open("groups.pickle", "wb") as file_w:
        pickle.dump(ls, file_w)
    if len(ls) != 0:
        return max([len(group.students) for group in ls])
    return 0


def write_students_information(ls: list[Student]) -> int:
    with open("students.pickle", "wb") as file_w:
        pickle.dump(ls, file_w)
    return len(ls)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file_r:
        data = pickle.load(file_r)
    return list(set(group.specialty.name for group in data))


def read_students_information() -> list:
    with open("students.pickle", "rb") as file_r:
        data = pickle.load(file_r)
    return list(student for student in data)
