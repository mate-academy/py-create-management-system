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


def write_groups_information(groups: list[Group]) -> int | list:
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            pickle.dump(group, pickle_file)
    if not groups:
        return []
    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
    return len(students)


def read_groups_information() -> list:
    objects = []
    result = []
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                obj = pickle.load(pickle_file)
                objects.append(obj)
            except EOFError:
                break
    for group in objects:
        if group.specialty.name not in result:
            result.append(group.specialty.name)
    return result


def read_students_information() -> list:
    objects = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                obj = pickle.load(pickle_file)
                objects.append(obj)
            except EOFError:
                break
    return objects
