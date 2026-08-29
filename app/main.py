from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: int
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: datetime
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as group_pickle:
        pickle.dump(groups, group_pickle)
        if groups:
            return max(len(group.students) for group in groups)
        return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_pickle:
        pickle.dump(students, students_pickle)
        return len(students)


def read_groups_information() -> list[str]:
    try:
        with open("groups.pickle", "rb") as g_pickle:
            read_group = pickle.load(g_pickle)
            specialties = {group.specialty.name for group in read_group}
            return list(specialties)
    except FileNotFoundError:
        return []


def read_students_information() -> list[Student]:
    try:
        with open("students.pickle", "rb") as s_pickle:
            students = pickle.load(s_pickle)
            return students
    except FileNotFoundError:
        return []
