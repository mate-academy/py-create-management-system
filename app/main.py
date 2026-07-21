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
    with open("groups.pickle", "wb") as target_file:
        pickle.dump(groups, target_file)

    return max(len(group.students) for group in groups) if groups else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as target_file:
        pickle.dump(students, target_file)

    return len(students)


def read_groups_information() -> set[str]:
    with open("groups.pickle", "rb") as source_file:
        groups = pickle.load(source_file)

    return set(group.specialty.name for group in groups)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as source_file:
        return pickle.load(source_file)
