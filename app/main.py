from dataclasses import dataclass
from datetime import date
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        max_students = 0
        for group in groups:
            if len(group.students) > max_students:
                max_students = len(group.students)
        pickle.dump(groups, f)

    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

        return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
        speciality_list = []
        for group in groups:
            speciality_list.append(group.specialty.name)

    return list(set(speciality_list))


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)

    return students
