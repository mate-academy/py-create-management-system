import dataclasses
import pickle
from datetime import datetime


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
    students: list


def write_groups_information(array: list) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(array, f)

    return max(len(i.students) for i in array) if array else 0


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        array_one = pickle.load(f)

    return list(set(num.specialty.name for num in array_one))


def write_students_information(array: list) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(array, f)

    return len(array)


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        array_one = pickle.load(f)

    return [num for num in array_one]
