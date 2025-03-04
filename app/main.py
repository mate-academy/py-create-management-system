import pickle
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: int
    last_name: int
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: int


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    if len(groups) == 0:
        return 0
    max_stud = len(groups[0].students)
    for group in groups:
        if len(group.students) > max_stud:
            max_stud = len(group.students)

    return max_stud


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information(file_name: str = "groups.pickle") -> list:
    with open(file_name, "rb") as file:
        groups = pickle.load(file)
        set_specialty_names = set([group.specialty.name for group in groups])
        return list(set_specialty_names)


def read_students_information(file_name: str = "students.pickle") -> list:
    with open(file_name, "rb") as file:
        return pickle.load(file)
