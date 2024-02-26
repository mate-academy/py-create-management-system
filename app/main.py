from dataclasses import dataclass
import pickle
from datetime import datetime


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: [Student]


def write_groups_information(groups: [Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    return max(
        [
            len(
                [st for st in group.students]
            )
            for group in groups
        ],
        default=0
    )
    # print(len([group.students for group in groups]))


def write_students_information(students: [Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len([student for student in students])


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    return set([group.specialty.name for group in groups])


def read_students_information() -> []:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)

    return students
