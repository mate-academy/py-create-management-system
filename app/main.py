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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]):
    with open('groups.pickle', 'wb') as file:
        max_number_of_students = 0
        for group in groups:
            pickle.dump(group, file)
            if len(group.students) > max_number_of_students:
                max_number_of_students = len(group.students)

        return max_number_of_students


def write_students_information(students: list[Student]):
    with open('students.pickle', 'wb') as file:
        for student in students:
            pickle.dump(student, file)
        return len(students)


def read_groups_information():
    all_groups = []
    with open('groups.pickle', 'rb') as file:
        while True:
            try:
                all_groups.append(pickle.load(file))
            except EOFError:
                break

    name_specialty = set()
    for grop in all_groups:
        name_specialty.add(grop.specialty.name)

    return name_specialty


def read_students_information():
    all_students = []
    with open('students.pickle', 'rb') as file:
        while True:
            try:
                all_students.append(pickle.load(file))
            except EOFError:
                break

    return all_students

