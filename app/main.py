import pickle
from dataclasses import dataclass
from datetime import date


@dataclass()
class Specialty:
    name: str
    number: int


@dataclass()
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass()
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as groups_pickle:
        pickle.dump(group_list, groups_pickle)
    return max([len(group.students) for group in group_list]) \
        if len(group_list) > 0 else 0


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as students_pickle:
        pickle.dump(students_list, students_pickle)
    return len(students_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as groups_pickle:
        groups = pickle.load(groups_pickle)
    return set([group.specialty.name for group in groups])


def read_students_information() -> list:
    with open("students.pickle", "rb") as student_pickle:
        students = pickle.load(student_pickle)
    return students
