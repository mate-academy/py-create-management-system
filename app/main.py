from dataclasses import dataclass
import pickle


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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    if groups:
        return max(len(gr_students.students) for gr_students in groups)
    return 0


def write_students_information(students: list[Student]) -> int:
    students_count = len(students)
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return students_count


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
        group_set = set()
        for group in groups:
            if group:
                group_set.add(group.specialty.name)
        return group_set


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        students = pickle.load(pickle_file)
        student_list = []
        for student in students:
            student_list.append(student)
        return student_list
