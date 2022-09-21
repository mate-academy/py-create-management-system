import dataclasses
from datetime import datetime
from typing import List
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
    students: List[Student]


def write_groups_information(written_data=List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(written_data, file)

    if written_data:
        return max(len(group.students) for group in written_data)

    return 0


def write_students_information(written_data=List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(written_data, file)

    return len(written_data)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups_info = pickle.load(file)

    result = set(
        group.specialty.name for group in groups_info
    )

    return result


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

    return students
