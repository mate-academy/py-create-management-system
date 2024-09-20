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
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(list_group: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        for group in list_group:
            pickle.dump(group, pickle_file)
        if list_group:
            return max(len(group.students) for group in list_group)
        else:
            return 0


def write_students_information(list_student: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for group in list_student:
            pickle.dump(group, pickle_file)
        return len(list_student)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as pickle_file:
        ls = []
        try:
            while True:
                list_group = pickle.load(pickle_file)
                ls.append(list_group.specialty.name)
        except EOFError:
            pass
    return set(ls)

    # return set(group.specialty.name for group in list_group)


def read_students_information() -> list:
    ls = []
    with open("students.pickle", "rb") as pickle_file:
        try:
            while True:
                list_students = pickle.load(pickle_file)
                ls.append(list_students)
        except EOFError:
            pass
    return ls
