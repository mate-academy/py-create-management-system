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
    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(groups, groups_file)

    return max([len(group.students) for group in groups], default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students, students_file)

    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_file:
        res = pickle.load(pickle_file)
    group_list = [group.specialty.name for group in res]

    return list(set(group_list))


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        res = pickle.load(pickle_file)

    return res
