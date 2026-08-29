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
    with open("groups.pickle", "wb") as groups_pickle_file:
        pickle.dump(groups, groups_pickle_file)

        return max(len(group.students) for group in groups) if groups else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_pickle_file:
        pickle.dump(students, students_pickle_file)

        return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as groups_pickle_file:
        groups = pickle.load(groups_pickle_file)

        return list(set(group.specialty.name for group in groups))


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as students_pickle_file:
        students = pickle.load(students_pickle_file)

        return [student for student in students]
