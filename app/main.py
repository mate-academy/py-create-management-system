import pickle
from dataclasses import dataclass
from datetime import date


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
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


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as handle:
        pickle.dump(groups, handle)
    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as handle:
        pickle.dump(students, handle)
    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as handle:
        read_file_group = pickle.load(handle)
    return list({group.specialty.name for group in read_file_group})


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as handle:
        read_file_students = pickle.load(handle)
    return read_file_students
