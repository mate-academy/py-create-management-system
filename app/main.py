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
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(list_of_the_group: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        result = []
        for students_group in list_of_the_group:
            student_count = len(students_group.students)
            result.append(student_count)
            pickle.dump(students_group, file)
        return max(result) if result else 0


def write_students_information(list_of_the_student: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        result = len(list_of_the_student)
        for student in list_of_the_student:
            pickle.dump(student, file)
    return result


def read_groups_information() -> list[str]:
    result = set()
    try:
        with open("groups.pickle", "rb") as file:
            while True:
                try:
                    group: Group = pickle.load(file)
                    result.add(group.specialty.name)
                except EOFError:
                    break
            return result
    except FileNotFoundError:
        return []


def read_students_information() -> list[Student]:
    result = []
    try:
        with open("students.pickle", "rb") as file:
            while True:
                try:
                    student = pickle.load(file)
                    result.append(student)
                except EOFError:
                    break
    except FileNotFoundError:
        return []
    return result
