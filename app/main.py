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
    mark: float
    has_scholarship: bool
    phone_number: str
    address: str
    average_mark: float = 0.0


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    students = set()
    for group in groups:
        for student in group.students:
            students.add((student.first_name, student.last_name))

    return len(students)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> list[str]:
    result = set()
    try:
        with open("groups.pickle", "rb") as f:
            for group in pickle.load(f):
                result.add(group.specialty.name)
    except EOFError:
        return []

    return list(result)


def read_students_information() -> list[Student]:
    result = []
    try:
        with open("students.pickle", "rb") as f:
            for student in pickle.load(f):
                result.append(student)
    except EOFError:
        return []

    return list(result)
