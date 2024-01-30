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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def read_groups_information(groups_file: str = "groups.pickle") \
        -> list[Specialty]:
    with open(groups_file, "rb") as file:
        try:
            while True:
                groups = pickle.load(file)
        except EOFError:
            pass

        specialties_names = set(group.specialty.name for group in groups)

        return list(specialties_names)


def write_groups_information(groups: list[Group]) -> int:
    total_student_counter = 0

    for group in groups:
        if total_student_counter < len(group.students):
            total_student_counter = len(group.students)

    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    return total_student_counter


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    if len(students) == 0:
        return 0
    return len(students)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        result = pickle.load(file)
    return result
