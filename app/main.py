import dataclasses
import pickle
from datetime import datetime


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
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
    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(groups, groups_file)
    try:
        return max(len(group.students) for group in groups)
    except ValueError:
        return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students, students_file)

    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as groups_file:
        groups = pickle.load(groups_file)

    specialties = set([group.specialty.name for group in groups])
    return list(specialties)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as students_file:
        students = pickle.load(students_file)

    return students
