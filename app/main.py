import dataclasses
from datetime import datetime
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: int
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(groups, groups_file)

    return max([len(group.students) for group in groups], default=0)


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students_list, students_file)

    return len(students_list)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as group_file:
        return list(
            set(group.specialty.name for group in pickle.load(group_file))
        )


def read_students_information() -> list:
    with open("students.pickle", "rb") as students_file:
        return list(pickle.load(students_file))
