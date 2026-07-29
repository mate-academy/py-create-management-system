import dataclasses
import pickle
from datetime import date


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
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
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    biggest_group = 0
    for group in groups:
        if len(group.students) > biggest_group:
            biggest_group = len(group.students)

    return biggest_group


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information(filename: str = "groups.pickle") -> list[str]:
    with open(filename, "rb") as file:
        groups = pickle.load(file)

    specialities = []
    for group in groups:
        if group.specialty.name not in specialities:
            specialities.append(group.specialty.name)

    return specialities


def read_students_information(
        filename: str = "students.pickle"
) -> list[Student]:
    with open(filename, "rb") as file:
        students = pickle.load(file)

    return students
