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
    birth_date: datetime.date
    average_mark: int
    has_scholarship: bool
    phone_number: str
    address: int


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as g:
        pickle.dump(group_list, g)
    return (max(len(group.students)
                for group in group_list)
            if group_list
            else 0
            )


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as s:
        pickle.dump(students_list, s)
    return len(students_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as g:
        groups = pickle.load(g)
    return set([group.specialty.name for group in groups])


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as s:
        students = pickle.load(s)
    return students
