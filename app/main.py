import pickle
from dataclasses import dataclass
from datetime import date


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as write_file:
        pickle.dump(groups, write_file)
    return max([len(group.students) for group in groups] + [0])


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as write_file:
        pickle.dump(students, write_file)
    return len(students)


def read_groups_information() -> list[Group]:
    with open("groups.pickle", "rb") as read_file:
        group_list = (pickle.load(read_file))
    return list(set([group.specialty.name for group in group_list]))


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as read_file:
        return pickle.load(read_file)
