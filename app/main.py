# write your code here
import pickle
import dataclasses
from datetime import date


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    students = []
    with open("groups.pickle", "wb") as file:
        for group in groups:
            students.append(len(group.students))
            pickle.dump(group, file)
    if students:
        return max(students)
    return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information() -> list:
    specialities = []
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
                specialities.append(group.specialty.name)
            except EOFError:
                break
    return list(set(specialities))


def read_students_information() -> list:
    students_arr = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                student = pickle.load(file)
                students_arr.append(student)
            except EOFError:
                break
    return students_arr
