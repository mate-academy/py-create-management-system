from dataclasses import dataclass
import pickle


@dataclass
class Specialty:
    name: str
    number: str


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
    specialty: str
    course: str
    students: list[Student]


def write_groups_information(group_info: list[Group]) -> int:
    max_student_count = 0
    with open("groups.pickle", "wb") as group_file:
        for group in group_info:
            pickle.dump(group, group_file)
            if len(group.students) > max_student_count:
                max_student_count = len(group.students)
    return max_student_count


def write_students_information(students_info: list[Student]) -> int:
    students_count = 0
    with open("students.pickle", "wb") as students_pickle:
        for student in students_info:
            pickle.dump(student, students_pickle)
            students_count += 1
    return students_count


def read_groups_information() -> list:
    specialties = set()
    with open("groups.pickle", "rb") as group_file:
        try:
            while True:
                group = pickle.load(group_file)
                specialties.add(group.specialty.name)
        except EOFError:
            pass
    return list(specialties)


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as students_pickle:
        try:
            while True:
                student = pickle.load(students_pickle)
                students.append(student)
        except EOFError:
            pass
    return students
