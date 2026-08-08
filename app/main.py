import pickle
from dataclasses import dataclass


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: int
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
    with open("groups.pickle", "wb") as file_info:
        pickle.dump(groups, file_info)
    result = [len(group.students) for group in groups]
    if result:
        return max(result)
    return []


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file_info:
        pickle.dump(students, file_info)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file_read:
        results = pickle.load(file_read)
        specialties = []
        for group in results:
            specialties.append(group.specialty.name)
    return set(specialties)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file_read:
        students = pickle.load(file_read)
    return students
