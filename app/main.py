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
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_number_of_students_in_group = 0
    with open("groups.pickle", "wb") as groups_pickle_file:
        for group in groups:
            pickle.dump(group, groups_pickle_file)
            if len(group.students) > max_number_of_students_in_group:
                max_number_of_students_in_group = len(group.students)
    return max_number_of_students_in_group


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as student_pickle_file:
        for student in students:
            pickle.dump(student, student_pickle_file)
    return len(students)


def read_groups_information() -> set:
    groups_specialties_names = []
    with open("groups.pickle", "rb") as groups_pickle_file:
        while True:
            try:
                group = pickle.load(groups_pickle_file)
            except EOFError:
                break
            else:
                groups_specialties_names.append(group.specialty.name)

    return set(groups_specialties_names)


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as students_pickle_file:
        while True:
            try:
                string = pickle.load(students_pickle_file)
            except EOFError:
                break
            else:
                students.append(string)

    return students
