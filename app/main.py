import pickle
import dataclasses
from typing import List


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(list_of_groups: List[Group]) -> list | int:
    with open("groups.pickle", "wb") as groups_file_write:
        for group in list_of_groups:
            pickle.dump(group, groups_file_write)

    return (
        max(
            [len(group.students) for group in list_of_groups]
        )
        if list_of_groups
        else 0
    )


def write_students_information(list_of_students: List[Student]) -> int:
    with open("students.pickle", "wb") as students_file_write:
        for student in list_of_students:
            pickle.dump(student, students_file_write)

    return len(list_of_students)


def read_groups_information() -> set:
    result = []

    with open("groups.pickle", "rb") as groups_file_read:
        try:
            while True:
                result.append(pickle.load(groups_file_read).specialty.name)
        except EOFError:
            pass

    return set(result)


def read_students_information() -> list:
    result = []

    with open("students.pickle", "rb") as students_file_read:
        try:
            while True:
                result.append(pickle.load(students_file_read))
        except EOFError:
            pass

    return result
