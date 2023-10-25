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


def write_groups_information(list_of_group: list[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as pickle_file:
        for group in list_of_group:
            students = len(group.students)
            if students > max_students:
                max_students = students
            pickle.dump(group, pickle_file)
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
    return len(students)


def read_groups_information() -> list[str]:
    objects = []
    names = set()
    with open("groups.pickle", "rb") as pickle_file:
        try:
            while True:
                group = pickle.load(pickle_file)
                objects.append(group)
        except EOFError:
            pass
    for group in objects:
        names.add(group.specialty.name)
    return list(names)


def read_students_information() -> list[Student]:
    objects = []
    with open("students.pickle", "rb") as pickle_file:
        try:
            while True:
                student = pickle.load(pickle_file)
                objects.append(student)
        except EOFError:
            pass
    return objects
