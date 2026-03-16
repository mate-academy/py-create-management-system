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
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:

    with open("groups.pickle", "wb") as pickle_file:
        if not groups:
            return 0

        for group in groups:
            pickle.dump(group, pickle_file)

    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:

    with open("students.pickle", "wb") as pickle_file:
        if not students:
            return 0
        for student in students:
            pickle.dump(student, pickle_file)

    return len(students)


def read_groups_information() -> list[str]:
    data_set = set()
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                data = pickle.load(pickle_file)
                data_set.add(data.specialty.name)
            except EOFError:
                return sorted(list(data_set))


def read_students_information() -> list[Student]:
    students_list = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                students_list.append(pickle.load(pickle_file))
            except EOFError:
                return students_list
