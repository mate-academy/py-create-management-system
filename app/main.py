import pickle
import dataclasses
from datetime import datetime


@dataclasses.dataclass
class Specialty:
    name: str
    number: str


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


def write_groups_information(list_of_groups: list[Group]) -> int:
    count_of_students_in_group: list[int] = []

    with open("groups.pickle", "wb") as pickle_file:
        for group in list_of_groups:
            pickle.dump(group, pickle_file)
            count_of_students_in_group.append(len(group.students))

    return max(count_of_students_in_group)


def write_students_information(list_of_students: list[Student]) -> int:
    count_of_students: int = 0

    with open("students.pickle", "wb") as pickle_file:
        for student in list_of_students:
            pickle.dump(student, pickle_file)
            count_of_students += 1

    return count_of_students


def read_groups_information(groups_file: str = "groups.pickle") -> list:
    with open(groups_file, "rb") as pickle_file:
        groups: list[Group] = pickle.load(pickle_file)

    return list({group.specialty.name for group in groups})


def read_students_information(students_file: str) -> list:
    with open(students_file, "rb") as pickle_file:
        students: list[Student] = pickle.load(pickle_file)

    return [student for student in students]
