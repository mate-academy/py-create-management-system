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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_students: list[Group]) -> int:
    number_of_students = []
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(group_students, pickle_file)
    for group in group_students:
        number_of_students.append(len(group.students))
    if group_students != []:
        return max(number_of_students)
    return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information() -> set:
    uniq_specialities = set()
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
        for group in groups:
            uniq_specialities.add(group.specialty.name)
    return uniq_specialities


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        students = pickle.load(pickle_file)
    return students
