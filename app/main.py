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
    average_mark: int
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
    max_students = max((len(group.students) for group in groups), default=0)
    return max_students


def write_students_information(student: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(student, file)

    return len(student)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    specialties = {group.specialty.name for group in groups}
    return list(specialties)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
