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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    if not groups:
        return 0

    total_students = max(len(group.students) for group in groups)

    with open("groups.pickle", "wb") as group_file:
        pickle.dump(groups, group_file)

    return total_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students, students_file)

    return len(students)


def read_groups_information(output_file: str = "groups.pickle") -> list:
    with open(output_file, "rb") as group_pick:
        groups = pickle.load(group_pick)

    specialties = set(group.specialty.name for group in groups)

    return list(specialties)


def read_students_information(output_file: str = "students.pickle") -> list:
    with open(output_file, "rb") as students_pick:
        students = list(pickle.load(students_pick))

    return students
