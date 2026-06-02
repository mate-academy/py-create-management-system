import pickle
from dataclasses import dataclass
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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(students: list[Group]) -> int:

    maximum_number_of_students_of_all_groups = max(
        [len(group.students) for group in students], default=0
    )

    with open("groups.pickle", "wb") as pickle_groups_file:
        pickle.dump(students, pickle_groups_file)

    return maximum_number_of_students_of_all_groups


def write_students_information(students: list[Student]) -> int:
    number_of_students = len(students)

    with open("students.pickle", "wb") as pickle_students_file:
        pickle.dump(students, pickle_students_file)

    return number_of_students


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as pickle_groups_file:
        load_pickle_groups_file = pickle.load(pickle_groups_file)

        return list(set(
            group.specialty.name for group in load_pickle_groups_file
        ))


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_students_file:
        return pickle.load(pickle_students_file)
