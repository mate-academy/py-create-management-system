import dataclasses
import pickle

from datetime import datetime


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

        for group in groups:
            pickle.dump(group, f)
        if len(groups) > 0:
            return max([len(group.students) for group in groups])
        else:
            return 0


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    specialty_names = set()
    for group in groups:
        specialty_names.add(group.specialty.name)

    return specialty_names


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
        return students
