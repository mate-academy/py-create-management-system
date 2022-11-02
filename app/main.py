import dataclasses
import pickle
from datetime import datetime
from typing import List, Set


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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file_group:
        pickle.dump(groups, file_group)
    return max([len(man.students) for man in groups]) \
        if len(groups) != 0 else 0


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file_students:
        pickle.dump(students, file_students)
    return len(students)


def read_groups_information() -> Set[str]:
    with open("groups.pickle", "rb") as file_group:
        groups_list = pickle.load(file_group)
    return {man.specialty.name for man in groups_list}


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file_student:
        list_students = pickle.load(file_student)
    return list_students
