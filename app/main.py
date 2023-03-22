from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass()
class Specialty:
    name: str
    number: int


@dataclass()
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass()
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_info: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(group_info, pickle_file)
    if group_info != []:
        return max([len(group.students) for group in group_info])


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    return set([group.specialty.name for group in groups])


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        our_students = pickle.load(file)
        return our_students
