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
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            pickle.dump(group, pickle_file)
    if groups:
        return max(len(group.students) for group in groups)
    else:
        return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information() -> set:
    result = set()
    with open("groups.pickle", "rb") as pickle_file:
        try:
            while True:
                group = pickle.load(pickle_file)
                result.add(group.specialty.name)
        except EOFError:
            pass
    return result


def read_students_information() -> list[Student]:
    result = []
    with open("students.pickle", "rb") as pickle_file:
        try:
            while True:
                students = pickle.load(pickle_file)
                result.extend(students)
        except EOFError:
            pass
    return result
