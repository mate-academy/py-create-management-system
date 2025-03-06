import dataclasses
import pickle
from datetime import datetime
from typing import List


@dataclasses.dataclass
class Specialty:
    name: str
    number: str


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

    @staticmethod
    def write_groups_information(groups: List["Group"],
                                 filename: str = "groups.pickle") -> int:
        with open(filename, "wb") as f:
            pickle.dump(groups, f)
        return max((len(group.students) for group in groups), default=0)

    @staticmethod
    def read_groups_information(filename: str = "groups.pickle") -> list:
        with open(filename, "rb") as f:
            groups = pickle.load(f)
        return list(set(group.speciality.name for group in groups))

    @staticmethod
    def write_students_information(students: list,
                                   filename: str = "students.pickle") -> int:
        with open(filename, "wb") as f:
            pickle.dump(students, f)
        return len(students)

    @staticmethod
    def read_students_information(filename: str = "students.pickle") -> str:
        with open(filename, "rb") as f:
            return pickle.load(f)
