import pickle
from datetime import datetime
from attr import dataclass


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
    students: list[Student]


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


def read_groups_information() -> list:
    try:
        with open("groups.pickle", "rb") as f:
            groups = pickle.load(f)
        specialties = {group.specialty.name for group in groups}
        return list(specialties)
    except FileNotFoundError:
        return []


def read_students_information() -> list:
    try:
        with open("students.pickle", "rb") as f:
            students = pickle.load(f)
        return students
    except FileNotFoundError:
        return []
