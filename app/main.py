import datetime
import pickle
from dataclasses import dataclass


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_groups:
        pickle.dump(groups, pickle_groups)
    return max(
        [len(group.students) for group in groups]
    ) if groups != [] else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_pickle:
        pickle.dump(students, students_pickle)
    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as pickle_groups:
        groups = pickle.load(pickle_groups)
    specialty_names = []
    for group in groups:
        if group.specialty.name not in specialty_names:
            specialty_names.append(group.specialty.name)
    return specialty_names


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as students_pickle:
        students = pickle.load(students_pickle)
    return students
