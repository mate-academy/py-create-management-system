import dataclasses
import pickle
from typing import Type, List


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: int


@dataclasses.dataclass
class Group:
    specialty: Type[Specialty]
    course: int
    students: List[Student]


def write_groups_information(information: List[Group]) -> int:
    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(information, groups_file)

    if not information:
        return 0

    max_number_of_students = max(len(group.students) for group in information)
    return max_number_of_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students, students_file)

    return len(students)


def read_groups_information() -> List[str]:
    with open("groups.pickle", "rb") as groups_file:
        groups_data = pickle.load(groups_file)

    specialties_names = list(
        set(group.specialty.name for group in groups_data)
    )
    return specialties_names


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as students_file:
        students_data = pickle.load(students_file)

    return students_data
