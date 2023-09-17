import dataclasses
import pickle
from datetime import datetime


@dataclasses.dataclass
class Specialty:
    name: str
    number: int

    def __str__(self) -> str:
        return self.name


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
    course: datetime
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(group_list, file)
    if len(group_list) == 0:
        return 0
    return max(len(group.students) for group in group_list)


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students_list, file)
        return len(students_list)


def read_groups_information() -> set[str]:
    with open("groups.pickle", "rb") as file:
        group_list = pickle.load(file)
    return set(str(group.specialty) for group in group_list)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        return pickle.load(file)
