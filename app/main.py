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
    average_mark: int | float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    student_counts = [0]

    for group in groups:
        student_counts.append(len(group.students))

    return max(student_counts)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        group = pickle.load(file)

    specialty_name = []

    for group in group:
        if group.specialty.name not in specialty_name:
            specialty_name.append(group.specialty.name)

    return specialty_name


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

        return students
