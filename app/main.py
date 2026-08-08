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
    with open("groups.pickle", "wb") as input_file:
        pickle.dump(groups, input_file)
        max_number_of_students = [len(group.students) for group in groups]
    return max(max_number_of_students) if groups else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as input_file:
        pickle.dump(students, input_file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as source_file:
        groups = pickle.load(source_file)

    specialties_names = list({group.specialty.name for group in groups})
    return specialties_names if len(groups) > 0 else []


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as source_file:
        students = pickle.load(source_file)
    return students
