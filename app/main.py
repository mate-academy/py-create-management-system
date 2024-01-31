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
    with open("groups.pickle", "wb") as groups_information:
        pickle.dump(groups, groups_information)
    if not groups:
        return 0
    return max([len(member.students) for member in groups])


def write_students_information(members: list[Student]) -> int:
    with open("students.pickle", "wb") as students_information:
        pickle.dump(members, students_information)
    return len(members)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as groups_file:
        groups = pickle.load(groups_file)
    return list(set([group.specialty.name for group in groups]))


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as student_file:
        students_list = pickle.load(student_file)
        return students_list
