import dataclasses
import pickle

from datetime import datetime


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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(
        groups: list[Group]
) -> int:
    count_students = []
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            count_students.append(len(group.students))
            pickle.dump(group, pickle_file)

    if count_students:
        return max(count_students)
    return count_students


def write_students_information(
        students: list[Student]
) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_file:
        name_groups = []
        try:
            while True:
                name_group = pickle.load(pickle_file).specialty.name
                if name_group not in name_groups:
                    name_groups.append(name_group)
        except EOFError:
            pass

    return name_groups


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        students = []
        try:
            while True:
                students.append(pickle.load(pickle_file))
        except EOFError:
            pass

    return students
