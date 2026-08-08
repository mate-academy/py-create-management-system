import pickle

from dataclasses import dataclass


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups_list, file)
    if groups_list:
        return max([len(group.students) for group in groups_list])


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students_list, file)
    return len(students_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups_list = pickle.load(file)
    return set([group.specialty.name for group in groups_list])


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students_list = pickle.load(file)
    return students_list
