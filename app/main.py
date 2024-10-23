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


def write_groups_information(object_group: list[Group]) -> int:

    with open("groups.pickle", "wb") as pickle_group:
        pickle.dump(object_group, pickle_group)

    max_students = 0
    for group in object_group:
        current_students = len(group.students)
        if current_students > max_students:
            max_students = current_students

    return max_students


def write_students_information(object_students: list[Student]) -> int:
    with open("students.pickle", "wb") as students:
        pickle.dump(object_students, students)

    return len(object_students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as pickle_read:
        object_group = pickle.load(pickle_read)

    specialty_names = set()
    for group in object_group:
        specialty_names.add(group.specialty.name)

    return specialty_names


def read_students_information() -> list:
    with open("students.pickle", "rb") as student_data:
        student_objects = pickle.load(student_data)
    return student_objects
