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


def write_groups_information(list_of_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as output_file:
        pickle.dump(list_of_groups, output_file)
    if len(list_of_groups) :
        return max(len(group.students) for group in list_of_groups)
    return 0


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as output_file:
        pickle.dump(list_of_students, output_file)
    return len(list_of_students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as input_file:
        groups = pickle.load(input_file)
    return list(set(group.specialty.name for group in groups))


def read_students_information() -> list:
    with open("students.pickle", "rb") as input_file:
        return pickle.load(input_file)
