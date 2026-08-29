from dataclasses import dataclass
import pickle
from typing import Set


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


def write_groups_information(groups: list[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            pickle.dump(group, pickle_file)
            max_students = max(max_students, len(group.students))
    return max_students


def write_students_information(students: list[Student]) -> int:
    num_students = len(students)
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
    return num_students


def read_groups_information() -> Set[str]:
    specialty_names: Set[str] = set()
    try:
        with open("groups.pickle", "rb") as pickle_file:
            while True:
                group: Group = pickle.load(pickle_file)
                specialty_names.add(group.specialty.name)
    except EOFError:
        pass
    except FileNotFoundError:
        print("Error: groups.pickle not found.")
    return specialty_names


def read_students_information() -> list[Student]:
    students: list[Student] = []
    try:
        with open("students.pickle", "rb") as pickle_file:
            while True:
                student: Student = pickle.load(pickle_file)
                students.append(student)
    except EOFError:
        pass
    except FileNotFoundError:
        print("Error: students.pickle not found.")
    return students
