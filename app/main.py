import os

import dataclasses

import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list


def write_groups_information(groups: list) -> int:
    if not groups:
        return 0

    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> set:
    specialties = set()
    file_path = "groups.pickle"

    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            groups = pickle.load(f)
            for group in groups:
                specialties.add(group.specialty.name)

    return specialties


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
