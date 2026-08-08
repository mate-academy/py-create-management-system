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


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as handle:
        pickle.dump(groups, handle)
    if len(groups) == 0:
        return 0

    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as handle:
        pickle.dump(students, handle)

    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as handle:
        group_list = pickle.load(handle)
    print(group_list)
    return list({group.specialty.name for group in group_list})


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as handle:
        student_list = pickle.load(handle)

    return student_list
