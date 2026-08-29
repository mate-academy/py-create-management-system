import pickle
from dataclasses import dataclass
import datetime


@dataclass
class Specialty:
    name: str
    number: int

    pass


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str

    pass


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]

    pass


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as source_file:
        pickle.dump(groups, source_file)
    return (max([len(group.students) for group in groups])
            if len(groups) > 0 else 0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as source_file:
        pickle.dump(students, source_file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as source_file:
        groups = pickle.load(source_file)
        return set([group.specialty.name for group in groups])


def read_students_information() -> list:
    with open("students.pickle", "rb") as source_file:
        students = pickle.load(source_file)
        return students
