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
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)

    max_num_of_groups = 0
    for group in groups:
        if len(group.students) > max_num_of_groups:
            max_num_of_groups = len(group.students)
    return max_num_of_groups


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
    specialties_names = [group.specialty.name for group in groups]
    return set(specialties_names)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        students = pickle.load(pickle_file)
    return [student for student in students]
