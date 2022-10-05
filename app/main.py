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
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list


def write_groups_information(array):
    with open("groups.pickle", "wb") as f:
        pickle.dump(array, f)
    lenght = [len(i.students) for i in array]
    return max(lenght) if lenght else 0


def read_groups_information():
    with open("groups.pickle", "rb") as f:
        arr = pickle.load(f)
    return list(set(i.specialty.name for i in arr))


def write_students_information(array):
    with open("students.pickle", "wb") as f:
        pickle.dump(array, f)
    return len(array)


def read_students_information():
    with open("students.pickle", "rb") as f:
        arr = pickle.load(f)
    return [i for i in arr]
