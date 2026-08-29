import dataclasses
import pickle
from typing import Any


@dataclasses.dataclass()
class Specialty:
    name: str
    number: int


@dataclasses.dataclass()
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass()
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(
        groups_info: list[Group]
) -> Any:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups_info, file)
    if not groups_info:
        return 0
    max_students = max(len(group.students) for group in groups_info)
    return max_students


def write_students_information(
        students_info: list[Student]
) -> Any:
    with open("students.pickle", "wb") as file:
        pickle.dump(students_info, file)
    return len(students_info)


def read_groups_information() -> Any:
    with open("groups.pickle", "rb") as file:
        group_list = pickle.load(file)
    return set(group.specialty.name for group in group_list)


def read_students_information() -> Any:
    with open("students.pickle", "rb") as file:
        stud_list = pickle.load(file)
    return stud_list
