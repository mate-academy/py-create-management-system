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
    student_counts = [len(group.students) for group in group_list]
    with open("groups.pickle", "wb") as f:
        pickle.dump(group_list, f)
    return max(student_counts) if student_counts else 0


def write_students_information(student_list: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in student_list:
            pickle.dump(student, f)
    return len(student_list)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as f:
        groups_data = pickle.load(f)
    groups_specialties = set()
    for group in groups_data:
        if hasattr(group, "specialty"):
            groups_specialties.add(group.specialty.name)
    return list(groups_specialties)


def read_students_information() -> list[Student]:
    students_list = []
    try:
        with open("students.pickle", "rb") as f:
            while True:
                try:
                    student = pickle.load(f)
                    students_list.append(student)
                except EOFError:
                    break
        return students_list
    except FileNotFoundError:
        return []
    except Exception as e:
        return []
