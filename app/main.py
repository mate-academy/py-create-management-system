from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(group_list, file)
    students_lenghts = [len(group.students) for group in group_list]
    if students_lenghts:
        return max(students_lenghts)
    else:
        return 0


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students_list, file)

    return len(students_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        group_list = pickle.load(file)

    return {group.specialty.name for group in group_list}


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students_list = pickle.load(file)

    return students_list
