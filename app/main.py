import dataclasses
from datetime import datetime
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: str | int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str | datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)

    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)

    return len(students)


def read_groups_information() -> list[str]:
    groups = []
    try:
        with open("groups.pickle", "rb") as f:
            while True:
                groups.append(pickle.load(f))
    except (EOFError, FileNotFoundError):
        pass

    specialty_names = []
    for group in groups:
        name = group.specialty.name
        if name not in specialty_names:
            specialty_names.append(name)

    return specialty_names


def read_students_information() -> list[Student]:
    students = []
    try:
        with open("students.pickle", "rb") as f:
            while True:
                students.append(pickle.load(f))
    except (EOFError, FileNotFoundError):
        pass

    return students
