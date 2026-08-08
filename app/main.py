import dataclasses
import datetime
import pickle
from typing import List


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
    course: float
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    maximum_students = 0

    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            if len(group.students) > maximum_students:
                maximum_students = len(group.students)
            pickle.dump(group, pickle_file)

    return maximum_students


def write_students_information(students: List[Student]) -> int:
    count_of_students = len(students)

    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)

    return count_of_students


def read_groups_information() -> List[str]:
    specialities_names = []

    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                group = pickle.load(pickle_file)
            except EOFError:
                break

            specialities_names.append(group.specialty.name)

    specialities_names = list(set(specialities_names))
    return specialities_names


def read_students_information() -> List[Student]:
    students = []

    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                student = pickle.load(pickle_file)
            except EOFError:
                break
            students.append(student)

    return students
