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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(groups, groups_file)

    if not groups:
        return 0

    total_students = max(len(group.students) for group in groups)
    return total_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students, students_file)

    return len(students)


def read_groups_information(output_file: str = "groups.pickle") -> list:
    with open(output_file, "rb") as groups_file:
        groups = pickle.load(groups_file)

    specialites = set(group.specialty.name for group in groups)
    return list(specialites)


def read_students_information(output_file: str = "students.pickle") -> list:
    with open(output_file, "rb") as students_file:
        students = list(pickle.load(students_file))

    return students
