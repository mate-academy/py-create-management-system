from dataclasses import dataclass
from datetime import date
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    students = []
    with open("groups.pickle", "wb") as pickle_file:
        for group in group_list:
            pickle.dump(group, pickle_file)
            for student in group.students:
                if student not in students:
                    students.append(student)

    return len(students)


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students_list:
            pickle.dump(student, pickle_file)

    return len(students_list)


def read_groups_information() -> list:
    specialties_names = []
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                group = pickle.load(pickle_file)
                if group.specialty.name not in specialties_names:
                    specialties_names.append(group.specialty.name)
            except EOFError:
                break

    return specialties_names


def read_students_information() -> list[Student]:
    students_instances = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                student = pickle.load(pickle_file)
                students_instances.append(student)
            except EOFError:
                break

    return students_instances
