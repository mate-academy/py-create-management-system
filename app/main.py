import pickle
from datetime import datetime
import dataclasses


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
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)
        return max([len(group.students) for group in groups], default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)
        return len(students)


def read_groups_information() -> list[str]:
    groups_list = []
    with open("groups.pickle", "rb") as f:
        while True:
            try:
                groups_list.append(pickle.load(f))
            except EOFError:
                break
    unique_specialties = set([group.specialty.name for group in groups_list])
    return list(unique_specialties)


def read_students_information() -> list[Student]:
    students_list = []
    with open("students.pickle", "rb") as f:
        while True:
            try:
                students_list.append(pickle.load(f))
            except EOFError:
                break
    return students_list
