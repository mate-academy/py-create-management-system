import dataclasses
from datetime import datetime
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number : int


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
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)

    return max(len(group.students) for group in groups) if groups else 0


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students_list, pickle_file)

    return len(students_list)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    return sorted({group.specialty.name for group in groups})


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
