import dataclasses
from datetime import datetime
import pickle


@dataclasses.dataclass
class Speciality:
    name: str
    number: str | int


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
    speciality: Speciality
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int | None:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    if len(groups) > 0:
        return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
        names = [group.speciality.name for group in groups]
    unique_names = list(set(names))
    return unique_names


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
