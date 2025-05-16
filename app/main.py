import dataclasses
from dataclasses import dataclass
from datetime import datetime
import pickle
from typing import List

@dataclass
class Specialty:
    name : str
    number: int

@dataclass
class Student:
    first_name: str
    last_name : str
    birth_date: int
    average_mark : float
    has_scholarship : bool
    phone_number: int
    address : str

@dataclass
class Group:
    specialty : Specialty
    course: int
    students: List

def write_groups_information(groups:List[Group]):
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    if groups == []:
        return []

    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]):
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)

def read_groups_information() -> List[str]:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
        specialty_name = {group.specialty.name for group in groups}
    return list(specialty_name)

def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)

    return students