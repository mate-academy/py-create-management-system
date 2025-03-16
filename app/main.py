from datetime import datetime
import pickle
import dataclasses


@dataclasses.dataclass()
class Specialty:
    name: str
    number: int


@dataclasses.dataclass()
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass()
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    max_student_count = 0
    for group in groups:
        if len(group.students) > max_student_count:
            max_student_count = len(group.students)
    return max_student_count


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups_list = pickle.load(file)
    specialties_set = set()
    for group in groups_list:
        specialties_set.add(group.specialty.name)
    return specialties_set


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students_list = pickle.load(file)
    all_students = []
    for student in students_list:
        all_students.append(student)
    return all_students
