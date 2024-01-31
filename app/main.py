from dataclasses import dataclass

import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: [Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    
    max_group = max(
        (group.students for group in groups if group.students), 
        key=len, default=[]
    )
    return len(max_group)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> tuple:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    specialty_names = set(gr.specialty.name for gr in groups)
    return tuple(specialty_names)


def read_students_information() -> tuple:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
