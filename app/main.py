from dataclasses import dataclass
from datetime import datetime
import pickle


GROUPS_FILENAME = "groups.pickle"
STUDENTS_FILENAME = "students.pickle"


@dataclass(unsafe_hash=True)
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


def write_groups_information(groups: list[Group]) -> int | None:
    with open(GROUPS_FILENAME, "wb") as file:
        pickle.dump(groups, file)
        if not groups:
            return 0
    return len(max(groups, key=lambda x: len(x.students)).students)


def write_students_information(students: list[Student]) -> int:
    with open(STUDENTS_FILENAME, "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list[str]:
    with open(GROUPS_FILENAME, "rb") as file:
        data = pickle.load(file)
    specialties = {item.specialty.name: 1 for item in data}
    return list(specialties.keys())


def read_students_information() -> list[Student]:
    with open(STUDENTS_FILENAME, "rb") as file:
        data = pickle.load(file)
    return data
