import dataclasses
from datetime import datetime
import pickle
from typing import List


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
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    group_stud_count = 0
    for group in groups:
        if len(group.students) > group_stud_count:
            group_stud_count = len(group.students)
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    return group_stud_count


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as fs_students:
        pickle.dump(students, fs_students)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as g_file:
        spec = pickle.load(g_file)
    return list(dict.fromkeys([stud.specialty.name for stud in spec]))


def read_students_information() -> list[str]:
    with open("students.pickle", "rb") as fs_students:
        students = pickle.load(fs_students)
    return students
