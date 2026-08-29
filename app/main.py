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


def write_groups_information(groups: list[Group]) -> int:
    student_counter = 0
    groups_list = []
    for group in groups:
        group_dict = {
            "specialty": group.specialty.name,
            "course": group.course,
            "students": group.students
        }
        groups_list.append(group_dict)
        if len(group.students) > student_counter:
            student_counter = len(group.students)
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups_list, f)
    return student_counter


def write_students_information(students: list[Student]) -> int:
    students_list = []
    student_counter = 0
    for student in students:
        students_list.append(student)
        student_counter += 1
    with open("students.pickle", "wb") as f:
        pickle.dump(students_list, f)
    return student_counter


def read_groups_information(file_name: str = "groups.pickle") -> list:
    specialities = []
    with open(file_name, "rb") as f:
        while True:
            try:
                groups_list = pickle.load(f)
                for group in groups_list:
                    specialty_name = group.get("specialty")
                    if specialty_name and specialty_name not in specialities:
                        specialities.append(specialty_name)
            except EOFError:
                break
    return specialities


def read_students_information(
        file_name: str = "students.pickle"
) -> list[Student]:
    students_list = []
    with open(file_name, "rb") as f:
        while True:
            try:
                students = pickle.load(f)
                for student in students:
                    students_list.append(student)
            except EOFError:
                break
    return students_list
