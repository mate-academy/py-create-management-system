from dataclasses import dataclass
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
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(lyceum_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(lyceum_groups, file)

    return max(len(group.students) for group in lyceum_groups)\
        if lyceum_groups\
        else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as file:
        lyceum_groups = pickle.load(file)

    return (
        list(set(group.specialty.name for group in lyceum_groups))
        if lyceum_groups
        else []
    )


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

    return students
