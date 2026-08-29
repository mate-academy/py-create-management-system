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
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups_list: list) -> int:
    with open("groups.pickle", "wb") as group_file:
        students = 0
        for group in groups_list:
            if len(group.students) > students:
                students = len(group.students)
            pickle.dump(group, group_file)
    return students


def write_students_information(students_list: list) -> int:
    with open("students.pickle", "wb") as students_file:
        count = 0
        for student in students_list:
            count += 1
            pickle.dump(student, students_file)
    return count


def read_groups_information() -> list:
    specialties_name = []
    with open("groups.pickle", "rb") as read_doc:
        while True:
            try:
                saved_group = pickle.load(read_doc)
                specialties_name.append(saved_group.specialty.name)
            except EOFError:
                break
    return list(set(specialties_name))


def read_students_information() -> list:
    list_of_students = []
    with open("students.pickle", "rb") as used_file:
        while True:
            try:
                student = pickle.load(used_file)
                list_of_students.append(student)
            except EOFError:
                break
    return list_of_students
