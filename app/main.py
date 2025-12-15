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
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list


def write_groups_information(groups: list[Group]) -> int:
    max_students_count = 0

    with open("groups.pickle", "wb") as file:

        pickle.dump(groups, file)

        for group in groups:

            max_students = len(group.students)

            if max_students > max_students_count:
                max_students_count = max_students

    return max_students_count


def write_students_information(students: list[Student]) -> int:
    students_count = 0

    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

        for student in students:
            students_count += 1

    return students_count


def read_groups_information() -> list[str]:
    specialties_set = set()

    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

        for group in groups:
            specialties_set.add(group.specialty.name)

    return list(specialties_set)


def read_students_information() -> list[Student]:
    students_list = []

    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

        for student in students:
            students_list.append(student)

    return students_list
