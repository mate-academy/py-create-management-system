import dataclasses
from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int

@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str

@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]

def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    return max(len(group.students) for group in groups) if groups else 0

def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)

def read_groups_information() -> set[str]:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    return set(group.specialty.name for group in groups)

def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        return pickle.load(f)
