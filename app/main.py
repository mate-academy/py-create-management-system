from typing import List, Set
from datetime import datetime
import dataclasses
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
    course: datetime
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:

    with open("groups.pickle", "wb") as groups_pickle:
        pickle.dump(groups, groups_pickle)

    if len(groups) == 0:
        return 0

    return max([len(group.students) for group in groups])


def write_students_information(students: List[Student]) -> int:

    with open("students.pickle", "wb") as students_pickle:
        pickle.dump(students, students_pickle)

    return len(students)


def read_groups_information() -> Set[str]:

    with open("groups.pickle", "rb") as groups_pickle:
        groups = pickle.load(groups_pickle)

        return set(group.specialty.name for group in groups)


def read_students_information() -> List[Student]:

    with open("students.pickle", "rb") as students_pickle:
        students = pickle.load(students_pickle)

        return students
