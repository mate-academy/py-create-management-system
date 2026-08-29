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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    students = [student
                for group in groups
                for student in group.students]
    unique_students = list(
        {student.average_mark: student
         for student in students}.values()
    )
    print(f"Unique Students: {unique_students} \n\n")
    return len(unique_students)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
    unique_speciality = list(
        {group.specialty.name: group.specialty.name
         for group in groups}.values()
    )
    return unique_speciality


def read_students_information() -> None:
    with open("students.pickle", "rb") as pickle_file:
        return pickle.load(pickle_file)
