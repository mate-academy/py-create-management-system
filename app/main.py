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
    students: list[Student]


def _save_to_pickle(filename: str, data: any) -> None:
    with open(filename, "wb") as f:
        pickle.dump(data, f)


def _load_from_pickle(filename: str) -> any:
    with open(filename, "rb") as f:
        return pickle.load(f)


def write_groups_information(groups: list[Group]) -> int:
    _save_to_pickle("groups.pickle", groups)
    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list[Student]) -> int:
    _save_to_pickle("students.pickle", students)
    return len(students)


def read_groups_information() -> list[str]:
    groups = _load_from_pickle("groups.pickle")
    return list({group.specialty.name for group in groups})


def read_students_information() -> list[Student]:
    return _load_from_pickle("students.pickle")
