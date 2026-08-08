from attr import dataclass
from datetime import datetime
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
    students: Student


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    if len(groups) > 0:
        students_max = []
        for group in groups:
            students_max.append(len(group.students))
        return max(students_max)
    else:
        return 0


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    specialties = set()
    for group in groups:
        specialties.add(group.specialty.name)
    return specialties


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
