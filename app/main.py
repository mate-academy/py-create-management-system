import pickle
import dataclasses as dc
from datetime import datetime
from typing import List


@dc.dataclass
class Specialty:
    name: str
    number: int


@dc.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dc.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int | None:
    with open("groups.pickle", "wb") as gp:
        pickle.dump(groups, gp)

    if groups:
        return max([len(group.students) for group in groups])
    return


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as sp:
        pickle.dump(students, sp)

    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pb:
        picload = pickle.load(pb)

    return list({group.specialty.name for group in picload})


def read_students_information() -> list:
    with open("students.pickle", "rb") as sp:
        picload = pickle.load(sp)

    return picload
