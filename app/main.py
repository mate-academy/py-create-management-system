from dataclasses import dataclass

import pickle


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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: tuple[Specialty]
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file_groups:
        pickle.dump(groups, file_groups)

    students_count = 0
    for group in groups:
        if len(group.students) > students_count:
            students_count = len(group.students)
    return students_count


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file_students:
        pickle.dump(students, file_students)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file_groups:
        groups = pickle.load(file_groups)
    return set([group.specialty.name for group in groups])


def read_students_information() -> list:
    with open("students.pickle", "rb") as file_students:
        loaded_group = pickle.load(file_students)

    return loaded_group
