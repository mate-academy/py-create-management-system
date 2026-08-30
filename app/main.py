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
    pickle.dump(groups, open("groups.pickle", "wb"))

    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list[Student]) -> int:
    pickle.dump(students, open("students.pickle", "wb"))

    return len(students)


def read_groups_information() -> set[str]:
    groups = pickle.load(open("groups.pickle", "rb"))

    return {group.specialty.name for group in groups}


def read_students_information() -> list[Student]:
    students = pickle.load(open("students.pickle", "rb"))

    return [student for student in students]
