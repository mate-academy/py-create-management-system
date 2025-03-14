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
    average_mark: int
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as group_file:
        pickle.dump(groups, group_file)

    if not groups:
        return 0

    max_amount_of_students = max(
        len(group.students)
        if group.students
        else 0
        for group in groups
    )
    return max_amount_of_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as student_file:
        pickle.dump(students, student_file)

    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as group_file:
        groups = pickle.load(group_file)

    specialist_name = set()
    for group in groups:
        specialist_name.add(group.specialty.name)

    return specialist_name


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as students_file:
        students = pickle.load(students_file)

    return students
