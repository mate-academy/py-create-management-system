import dataclasses
import pickle
from datetime import datetime


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
    with open("groups.pickle", "wb") as group_info:
        pickle.dump(groups, group_info)
    return max([len(group.students) for group in groups], default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as student_info:
        pickle.dump(students, student_info)
    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as group_info:
        groups = pickle.load(group_info)
    seen = set()
    return [
        group.specialty.name for group in groups if not (
            group.specialty.name in seen or seen.add(group.specialty.name
                                                     )
        )
    ]


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as student_info:
        students = pickle.load(student_info)
    return students
