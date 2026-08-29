from dataclasses import dataclass
from datetime import datetime
from typing import List
import pickle


@dataclass
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
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as groups_file:
        for group in groups:
            pickle.dump(group, groups_file)

    if not groups:
        return 0

    return max(len(group.students) for group in groups)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        for student in students:
            pickle.dump(student, students_file)

    return len(students)


def read_groups_information() -> List[str]:
    specialties: List[str] = []
    seen = set()

    try:
        with open("groups.pickle", "rb") as groups_file:
            while True:
                group: Group = pickle.load(groups_file)
                name = group.specialty.name
                if name not in seen:
                    seen.add(name)
                    specialties.append(name)
    except FileNotFoundError:
        pass
    except EOFError:
        pass
    return specialties


def read_students_information() -> List[Student]:
    students: List[Student] = []

    try:
        with open("students.pickle", "rb") as students_file:
            while True:
                student: Student = pickle.load(students_file)
                students.append(student)
    except FileNotFoundError:
        pass
    except EOFError:
        pass

    return students
