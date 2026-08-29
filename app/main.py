import dataclasses
from datetime import datetime
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    list_of_numbers = []
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
            list_of_numbers.append(len(group.students))
        if not list_of_numbers:
            return 0
        maximum_number = max(list_of_numbers)
    return maximum_number


def write_students_information(students: list[Student]) -> int:
    number = 0
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
            number += 1
    return number


def read_groups_information() -> list:
    list_of_names = []
    groups_information = []
    seen = set()
    with open("groups.pickle", "rb") as file:
        try:
            while True:
                obj = pickle.load(file)
                groups_information.append(obj)
        except EOFError:
            pass
        for group in groups_information:
            name = group.specialty.name
            if name not in seen:
                list_of_names.append(name)
                seen.add(name)
            else:
                pass
        return list_of_names


def read_students_information() -> list:
    list_of_students = []
    students_information = []
    with open("students.pickle", "rb") as file:
        try:
            while True:
                single_information = pickle.load(file)
                students_information.append(single_information)
        except EOFError:
            pass
        for student in students_information:
            list_of_students.append(student)
        return list_of_students
