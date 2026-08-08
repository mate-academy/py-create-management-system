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


def write_groups_information(group_data: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        for group in group_data:
            pickle.dump(group, f)
    students = []
    for group in group_data:
        for student in group.students:
            if student not in students:
                students.append(student)
    return len(students)


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students_list:
            pickle.dump(student, f)
    return len(students_list)


def read_groups_information() -> list:
    data = []
    with open("groups.pickle", "rb") as f:
        while True:
            try:
                group_pickle = pickle.load(f)
                data.append(group_pickle)
            except Exception:
                break
    result = []
    for group in data:
        if group.specialty.name not in result:
            result.append(group.specialty.name)
    return result


def read_students_information() -> list:
    data = []
    with open("students.pickle", "rb") as f:
        while True:
            try:
                student = pickle.load(f)
                data.append(student)
            except Exception:
                break
    return data
