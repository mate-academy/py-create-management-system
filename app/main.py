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


def write_groups_information(list_of_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(list_of_groups, file)

    return max(
        len(group.students) for group in list_of_groups
    ) if list_of_groups else 0


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(list_of_students, file)

    return len(list_of_students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as file:
        list_of_groups = pickle.load(file)

    return list(
        dict.fromkeys(group.specialty.name for group in list_of_groups).keys()
    )


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        list_of_students = pickle.load(file)

    return list_of_students
