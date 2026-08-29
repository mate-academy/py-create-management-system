from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass
class Specialty:
    name : str
    number : int


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
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_students = 0
    for group in groups:
        max_students = max(len(group.students), max_students)

    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
        return len(students)


def read_groups_information() -> list:
    result = set()
    with open("groups.pickle", "rb") as file:
        data = pickle.load(file)

        for group in data:
            result.add(group.specialty.name)

        return result


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        data = pickle.load(file)
        return [
            Student(student.first_name,
                    student.last_name,
                    student.birth_date,
                    student.average_mark,
                    student.has_scholarship,
                    student.phone_number,
                    student.address) for student in data]
