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
    phone_number: int | str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_ls: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickled_group:
        pickle.dump(group_ls, pickled_group)
    max_students = 0
    for group in group_ls:
        if max_students < len(group.students):
            max_students = len(group.students)
    return max_students


def write_students_information(student_ls: list[Student]) -> int:
    with open("students.pickle", "wb") as pickled_students:
        pickle.dump(student_ls, pickled_students)
    return len(student_ls)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickled_group:
        groups = pickle.load(pickled_group)
        specialty_set = set()
        for group in groups:
            specialty_set.add(group.specialty.name)
        return list(specialty_set)


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickled_students:
        student_ls = pickle.load(pickled_students)
    return student_ls
