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
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
    if not groups:
        return 0
    return max(
        len(group.students) for group in groups
    )


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set[str]:
    specialties_names = set()
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
                specialties_names.add(group.specialty. name)
            except EOFError:
                break
    return specialties_names


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
