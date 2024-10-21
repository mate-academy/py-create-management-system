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
    course: str
    students: list[Student]


def write_groups_information(lyceum_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as gs:
        pickle.dump(lyceum_groups, gs)
    max_students_in_group = (
        max(len(group.students) for group in lyceum_groups)
        if lyceum_groups else 0
    )
    return max_students_in_group


def write_students_information(all_students: list[Student]) -> int:
    with open("students.pickle", "wb") as st:
        pickle.dump(all_students, st)
    return len(all_students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as gp:
        lyceum_groups = pickle.load(gp)
    specialties = {group.specialty.name for group in lyceum_groups}
    return list(specialties)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as sp:
        all_students = pickle.load(sp)
        return all_students
