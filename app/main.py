import dataclasses
from datetime import datetime
import pickle


@dataclasses.dataclass()
class Specialty:
    name: str
    number: int


@dataclasses.dataclass()
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass()
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    pickle.dump(groups, open("groups.pickle", "wb"))
    max_students = 0
    if len(groups) > 0:
        max_students = max([len(group.students) for group in groups])
    return max_students


def write_students_information(students: list[Student]) -> int:
    pickle.dump(students, open("students.pickle", "wb"))
    return len(students)


def read_groups_information() -> list[str]:
    groups = pickle.load(open("groups.pickle", "rb"))
    result = []
    if len(groups) > 0:
        result = [group.specialty.name for group in groups]
    return list(set(result))


def read_students_information() -> list[Student]:
    return pickle.load(open("students.pickle", "rb"))
