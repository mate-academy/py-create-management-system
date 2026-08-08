import dataclasses
from datetime import datetime
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: str


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


def write_groups_information(
        groups: list[Group],
        filename: str = "groups.pickle"
) -> int:
    with open(filename, "wb") as file:
        pickle.dump(groups, file)
    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(
        students: list[Student],
        filename: str = "students.pickle"
) -> int:
    with open(filename, "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information(
        filename: str = "groups.pickle"
) -> set:
    with open(filename, "rb") as file:
        groups = pickle.load(file)
    return set(group.specialty.name for group in groups)


def read_students_information(
        filename: str = "students.pickle"
) -> list[Student]:
    with open(filename, "rb") as file:
        students = pickle.load(file)
    return [student for student in students]
