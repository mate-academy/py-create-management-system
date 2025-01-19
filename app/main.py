import pickle
from dataclasses import dataclass
from datetime import datetime
from typing import List


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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list


def read_groups_information() -> List[str]:
    try:
        with open("groups.pickle", "rb") as file:
            groups = pickle.load(file)

        if not groups:
            return []
        specialties = set(group.specialty.name for group in groups)
        return list(specialties)

    except FileNotFoundError:
        print(f"file {groups.pickle} dont find")
        return []


def read_students_information() -> List[Student]:
    try:
        with open("students.pickle", "rb") as file:
            students = pickle.load(file)
        return students
    except FileNotFoundError:
        print(f"file {students.pickle} dont find")
        return []


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    if not groups:
        return 0

    max_students = max(len(group.students) for group in groups)
    return max_students
