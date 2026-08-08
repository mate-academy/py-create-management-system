import dataclasses
from datetime import date
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date.today()
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups):
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    return max((len(group.students) for group in groups), default=0)


def write_students_information(student):
    with open("students.pickle", "wb") as f:
        pickle.dump(student, f)
    return len(student)


def read_groups_information():
    with open("groups.pickle", "rb") as f:
        all_groups = pickle.load(f)
    return [*set(group.specialty.name for group in all_groups)]


def read_students_information():
    with open("students.pickle", "rb") as f:
        all_students = pickle.load(f)
        return all_students
