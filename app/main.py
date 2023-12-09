import pickle
from dataclasses import dataclass
from datetime import date


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as groups:
        pickle.dump(group_list, groups)
        try:
            max_students_in_group = max(
                [len(group.students) for group in group_list]
            )
            return max_students_in_group
        except ValueError:
            return 0


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as students:
        pickle.dump(students_list, students)
        return len(students_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
        return set(group.specialty.name for group in groups)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        return pickle.load(file)
