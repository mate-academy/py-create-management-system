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
    max_students_count = 0
    for group in groups:
        max_students_count = max(max_students_count, len(group.students))

    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    return max_students_count


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information(filename: str = "groups.pickle") -> list[str]:
    try:
        with open(filename, "rb") as file:
            groups: list[Group] = pickle.load(file)
    except EOFError:
        groups = []

    specialty_names: list[str] = []
    for group in groups:
        name = group.specialty.name
        if name not in specialty_names:
            specialty_names.append(name)

    return specialty_names


def read_students_information(
        filename: str = "students.pickle"
) -> list[Student]:
    try:
        with open(filename, "rb") as file:
            students: list[Student] = pickle.load(file)
    except EOFError:
        return []
    return students
