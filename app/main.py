from dataclasses import dataclass
from datetime import datetime
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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        students_count = 0
        for group in groups:
            pickle.dump(group, pickle_file)
            if len(group.students) > students_count:
                students_count = len(group.students)
    return students_count


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information() -> set[str]:
    specialties = set()
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                obj = pickle.load(pickle_file)
            except EOFError:
                break
            if isinstance(obj, list):
                for item in obj:
                    if isinstance(item, Group):
                        specialties.add(item.specialty.name)
            else:
                if isinstance(obj, Group):
                    specialties.add(obj.specialty.name)
    return specialties


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                obj = pickle.load(pickle_file)
            except EOFError:
                break
            if isinstance(obj, list):
                for item in obj:
                    if isinstance(item, Student):
                        students.append(item)
            else:
                if isinstance(obj, Student):
                    students.append(obj)
    return students
