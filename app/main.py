import dataclasses
import pickle
from datetime import datetime


@dataclasses.dataclass()
class Specialty:
    name: str
    number: int


@dataclasses.dataclass()
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
    students_count = [len(group.students) for group in groups]
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    return max(students_count) if len(students_count) > 0 else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    if len(groups) == 0:
        return []
    specialities_names = [group.specialty.name for group in groups]
    return list(dict.fromkeys(specialities_names))


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
