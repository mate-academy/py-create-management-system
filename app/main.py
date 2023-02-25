from typing import List
from datetime import datetime
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
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    if len(groups) != 0:
        max_students = max(len(g.students) for g in groups)
    else:
        max_students = []
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> List[str]:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    specialties = set(g.specialty.name for g in groups)
    return list(specialties)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as f:
        students = []
        while True:
            try:
                student = pickle.load(f)
                students.append(student)
            except EOFError:
                break
    return students
