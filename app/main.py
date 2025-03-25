import pickle
import dataclasses
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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(group_list, file)
    if len(group_list) != 0:
        return max([len(group.students) for group in group_list])
    return 0


def write_students_information(studen_list: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(studen_list, file)
    return len(studen_list)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as file:
        content = pickle.load(file)

    specialties = set()

    for group in content:
        specialties.add(group.specialty.name)
    return list(specialties)


def read_students_information() -> None:
    with open("students.pickle", "rb") as file:
        return pickle.load(file)
