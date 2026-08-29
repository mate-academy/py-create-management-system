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
    phone_number : str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file_with_groups:
        pickle.dump(groups, file_with_groups)

    max_count = 0
    for group in groups:
        count_in_group = len(group.students)
        if count_in_group > max_count:
            max_count = count_in_group
    return max_count


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file_with_students:
        pickle.dump(students, file_with_students)

    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as file_with_groups:
        groups = pickle.load(file_with_groups)
        specialities = set()
        for group in groups:
            specialities.add(group.specialty.name)

    return list(specialities)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file_with_students:
        students = pickle.load(file_with_students)

    return students
