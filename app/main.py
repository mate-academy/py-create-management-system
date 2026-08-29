import os.path
from datetime import datetime
import dataclasses
import pickle


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
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int | None:
    if groups:
        with open("groups.pickle", "wb") as groups_info_file:
            for group in groups:
                pickle.dump(group, groups_info_file)

        return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_info_file:
        for student in students:
            pickle.dump(student, students_info_file)

    return len(students)


def read_groups_information() -> list:
    result = []
    if os.path.exists("groups.pickle"):
        with open("groups.pickle", "rb") as groups_info_file:
            while True:
                try:
                    result.append(pickle.load(groups_info_file).specialty.name)
                except EOFError:
                    break

    return list(set(result))


def read_students_information() -> list:
    result = []
    with open("students.pickle", "rb") as students_info_file:
        while True:
            try:
                result.append(pickle.load(students_info_file))
            except EOFError:
                break

    return result
