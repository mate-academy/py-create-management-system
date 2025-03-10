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


@dataclasses.dataclass()
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as groups_file:
        pickle.dump([group for group in groups], groups_file)
    students = [len(group.students) for group in groups] + [0]
    return max(students)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump([student for student in students], students_file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as groups_file:
        groups = pickle.load(groups_file)
        specialty = list(set(group.specialty.name for group in groups))
        return specialty


def read_students_information() -> list:
    with open("students.pickle", "rb") as students_file:
        students = pickle.load(students_file)
        return students
