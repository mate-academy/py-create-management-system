import dataclasses
from datetime import datetime
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
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as data:
        pickle.dump(groups, data)

    if groups:
        return max(len(student.students) for student in groups)
    else:
        return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as data:
        pickle.dump(students, data)

    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as data:
        groups = pickle.load(data)

    return set([group.specialty.name for group in groups])


def read_students_information() -> list:
    with open("students.pickle", "rb") as data:
        students = pickle.load(data)
    return students
