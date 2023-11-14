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


def write_groups_information(all_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pcl_group_file:
        pickle.dump(all_groups, pcl_group_file)
        result = []
        for group in all_groups:
            for student in group.students:
                if student not in result:
                    result.append(student)
        return len(result)


def write_students_information(all_students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(all_students, students_file)
        return len(all_students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as student:
        groups = pickle.load(student)
        return set(group.specialty.name for group in groups)


def read_students_information() -> list:
    with open("students.pickle", "rb") as text:
        return pickle.load(text)
