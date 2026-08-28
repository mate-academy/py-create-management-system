import pickle
from dataclasses import dataclass


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
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
        for group in groups:
            pickle.dump(group, file)

    return max(len(group.students) for group in groups) if groups != [] else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)

    return len(students)


def read_groups_information() -> set:
    result = set()

    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
                result.add(group.specialty.name)
            except EOFError:
                break

    return result


def read_students_information() -> list:
    result = []

    with open("students.pickle", "rb") as file:
        while True:
            try:
                student = pickle.load(file)
                result.append(student)
            except EOFError:
                break

    return result
