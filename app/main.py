import pickle
import dataclasses
from datetime import datetime
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


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file_in:
        pickle.dump(groups, file_in)
    if groups:
        return max(len(group.students) for group in groups)

    return 0


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information(filename: str = "groups.pickle") -> List[str]:
    with open(filename, "rb") as file:
        groups = pickle.load(file)

    return list({group.specialty.name for group in groups})


def read_students_information(
        filename: str = "students.pickle"
) -> List[Student]:
    with open(filename, "rb") as file:
        students = pickle.load(file)

    return students
