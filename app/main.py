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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as file:
        pickle.dump(group_list, file)

    for group in group_list:
        if len(group.students) > max_students:
            max_students = len(group.students)
    return max_students


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students_list, file)
    return len(students_list)


def read_groups_information() -> list:
    specialty_names = set()

    try:
        with open("groups.pickle", "rb") as file:
            groups = pickle.load(file)
            for group in groups:
                specialty_names.add(group.specialty.name)

    except FileNotFoundError:
        print("File not found!")
        return []
    except EOFError:
        print("File is empty!")
        return []
    except Exception as e:
        print("Error" + e)
        return []

    return list(specialty_names)


def read_students_information() -> list:
    student_list = []

    try:
        with open("students.pickle", "rb") as file:
            student_list = pickle.load(file)

    except FileNotFoundError:
        print("File not found!")
        return []
    except EOFError:
        print("File is empty!")
        return []
    except Exception as e:
        print("Error" + e)
        return []

    return student_list
