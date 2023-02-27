from dataclasses import dataclass
from pickle import load, dump
from datetime import date


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name : str
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


def write_groups_information(group_ls: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        dump(len(group_ls), file)
        for group in group_ls:
            dump(group, file)
    return max(len(group.students) for group in group_ls) if group_ls else 0


def write_students_information(student_ls: list[Group]) -> int:
    with open("students.pickle", "wb") as file:
        dump(len(student_ls), file)
        for stud in student_ls:
            dump(stud, file)
    return len(student_ls)


def read_groups_information() -> list:
    spec_set = set()
    with open("groups.pickle", "rb") as file:
        num = load(file)
        for _ in range(num):
            group = load(file)
            spec_set.add(group.specialty.name)
    return list(spec_set)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        num = load(file)
        stud_ls = [load(file) for _ in range(num)]
    return stud_ls
