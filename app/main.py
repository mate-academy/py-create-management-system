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
    with open("groups.pickle", "wb") as file_groups:
        pickle.dump(list_of_groups, file_groups)
    return max([len(group.students) for group in list_of_groups], default=0)


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as file_students:
        pickle.dump(list_of_students, file_students)
    return len(list_of_students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as file_groups:
        list_groups = pickle.load(file_groups)
    return list(set([group.specialty.name for group in list_groups]))


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file_students:
        return pickle.load(file_students)
