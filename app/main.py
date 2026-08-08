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


def write_groups_information(groups: list[Group]) -> list:
    with open("groups.pickle", "wb") as pickle_groups:
        pickle.dump(groups, pickle_groups)

    try:
        groups = max(len(group.students) for group in groups)
    except ValueError:
        print("Student's group is empty.")

    return groups


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_students:
        pickle.dump(students, pickle_students)

    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_groups:
        groups = pickle.load(pickle_groups)

    return list(set([group.specialty.name for group in groups]))


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_students:
        students = pickle.load(pickle_students)

    return students
