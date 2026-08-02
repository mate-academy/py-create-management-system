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
    with open("groups.pickle", "wb") as groups_file:
        for group in groups:
            pickle.dump(group, groups_file)

    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        for student in students:
            pickle.dump(student, students_file)

    return len(students)


def read_pickled_items(file_name: str) -> list:
    items = []
    with open(file_name, "rb") as source_file:
        while True:
            try:
                items.append(pickle.load(source_file))
            except EOFError:
                break
    return items


def read_groups_information() -> list[str]:
    groups = read_pickled_items("groups.pickle")
    specialty_names = []

    for group in groups:
        name = group.specialty.name
        if name not in specialty_names:
            specialty_names.append(name)

    return specialty_names


def read_students_information() -> list[Student]:
    return read_pickled_items("students.pickle")
