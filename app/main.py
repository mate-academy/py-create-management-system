import pickle
from dataclasses import dataclass
from datetime import date
# hello


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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    std_count = []
    with open("groups.pickle", "wb") as file:
        for group in group_list:
            [
                std_count.append(std)
                for std in group.students
                if std not in std_count
            ]
            pickle.dump(group, file)
    return len(std_count)


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for std in students_list:
            pickle.dump(std, file)
    return len(students_list)


def read_groups_information() -> set:
    nlist = set()
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
            except EOFError:
                break
            nlist.add(group.specialty.name)
    return nlist


def read_students_information() -> list[Student]:
    nlist = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                std = pickle.load(file)
            except EOFError:
                break
            nlist.append(std)
    return nlist
