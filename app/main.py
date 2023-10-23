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


def write_groups_information(groups: list[Group]) -> any:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    st = [len(group.students) for group in groups]
    if len(st) > 0:
        return max(st)
    return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> list[Group]:
    with open("groups.pickle", "rb") as f:
        groups_info = pickle.load(f)
    return list(set([group.specialty.name for group in groups_info]))


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return [student for student in students]
