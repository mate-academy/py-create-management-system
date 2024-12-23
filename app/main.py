import dataclasses
from datetime import datetime
import pickle
from typing import List


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
    students: List[Student]


def write_groups_information(
        groups: List[Group],
        file_name: str = "groups.pickle"
) -> int:
    with open(file_name, "wb") as group_file:
        pickle.dump(groups, group_file)
    return max((len(group.students) for group in groups), default=0)


def write_students_information(
        students: List[Student],
        file_name: str = "students.pickle"
) -> int:
    with open(file_name, "wb") as student_file:
        pickle.dump(students, student_file)
    return len(students)


def read_groups_information(
        file_name: str = "groups.pickle"
) -> List[str]:
    with open(file_name, "rb") as group_file:
        groups = pickle.load(group_file)
    return list({group.specialty.name for group in groups})


def read_students_information(
        file_name: str = "students.pickle"
) -> List[Student]:
    with open(file_name, "rb") as student_file:
        students = pickle.load(student_file)
    return students
