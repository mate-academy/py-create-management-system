import pickle
import dataclasses
from datetime import datetime


@dataclasses.dataclass
class Specialty:
    name : str
    number : int


@dataclasses.dataclass
class Student:
    first_name : str
    last_name : str
    birth_date : datetime
    average_mark : float
    has_scholarship : bool
    phone_number : int
    address : str


@dataclasses.dataclass
class Group:
    specialty : Specialty
    course : int
    students : list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information(groups_pickle: str = "groups.pickle") -> set:
    with open(groups_pickle, "rb") as f:
        groups = pickle.load(f)

    specialty_list = {group.specialty.name for group in groups}
    return specialty_list


def read_students_information(
        students_pickle: str = "students.pickle"
) -> list[Student]:
    with open(students_pickle, "rb") as f:
        students = pickle.load(f)

    return students
