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
    birth_date: int
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: str
    course: int
    students: list


def write_groups_information(groups: list) -> None:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    students_count = []
    for group in groups:
        students_count.append(len(group.students))
        return max(students_count)


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

        specialties = set()
        for group in groups:
            specialties.add(group.specialty)

        return specialties


def read_students_information() -> None:
    with open("students.pickle", "rb") as file:
        list_of_students = pickle.load(file)
    return list_of_students
