from dataclasses import dataclass, field
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
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student] = field(default_factory=list)


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        for instance in groups:
            pickle.dump(instance, pickle_file)
    return max(len(group.students) for group in groups) if groups else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for instance in students:
            pickle.dump(instance, pickle_file)
    return len(students)


def read_groups_information() -> list:
    groups = []
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                instance = pickle.load(pickle_file)
                groups.append(instance)
            except EOFError:
                break
    return list(set([group.specialty.name for group in groups]))


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                instance = pickle.load(pickle_file)
                students.append(instance)
            except EOFError:
                break
    return students
