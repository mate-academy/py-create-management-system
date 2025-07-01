from dataclasses import dataclass
from datetime import datetime
from typing import List
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
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    file_name = "groups.pickle"

    with open(file_name, "wb") as ws:
        pickle.dump(groups, ws)

    if not groups:
        return 0
    else:
        return max(len(group.students) for group in groups)


def write_students_information(students: List[Student]) -> int:
    file_name = "students.pickle"
    ws = open(file_name, "wb")
    for student in students:
        pickle.dump(student, ws)
    ws.close()
    return len(students)


def read_groups_information() -> List[str]:
    file_name = "groups.pickle"
    specialty_names = set()

    try:
        with open(file_name, "rb") as rs:
            groups = pickle.load(rs)
            for group in groups:
                specialty_names.add(group.specialty.name)
    except FileNotFoundError:
        return []
    except EOFError:
        return []

    return list(specialty_names)


def read_students_information() -> List[Student]:
    file_name = "students.pickle"
    students = []

    with open(file_name, "rb") as rs:
        while True:
            try:
                student = pickle.load(rs)
                students.append(student)
            except EOFError:
                break

    return students
