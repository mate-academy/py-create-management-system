import dataclasses
import pickle
from datetime import date


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
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
    with open("groups.pickle", "wb") as pickle_file:
        # noinspection PyTypeChecker
        pickle.dump(groups, pickle_file)

    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        # noinspection PyTypeChecker
        pickle.dump(students, pickle_file)

    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)

    return list({group.specialty.name for group in groups})


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        return pickle.load(pickle_file)
