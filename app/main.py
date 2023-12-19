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
    birth_date: int
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_information: list[Group]) -> int:
    with (open("groups.pickle", "wb") as pickle_file):
        for group_inst in group_information:
            pickle.dump(group_inst, pickle_file)

        max_number_students = 0 if not group_information else max(
            len(group.students) for group in group_information
        )

    return max_number_students


def write_students_information(student_information: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        number_of_students = 0
        for student_inst in student_information:
            pickle.dump(student_inst, pickle_file)
            number_of_students += 1
    return number_of_students


def read_groups_information() -> list:
    specialty = []
    with open("groups.pickle", "rb") as pickle_file:

        try:
            while True:
                groups = pickle.load(pickle_file)
                specialty.append(groups.specialty.name)
        except EOFError:
            return list(set(specialty))


def read_students_information() -> list:
    list_of_student_instance = []
    with open("students.pickle", "rb") as pickle_file:

        try:
            while True:
                students = pickle.load(pickle_file)
                list_of_student_instance.append(students)
        except EOFError:
            return list_of_student_instance
