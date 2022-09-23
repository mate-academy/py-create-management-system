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
    course: str
    students: list


def write_groups_information(group_list):
    students_number = []
    with open("groups.pickle", "wb") as f:
        for inst in group_list:
            pickle.dump(inst, f)
            students_number.append(len(inst.students))
    if len(students_number) > 0:
        return max(students_number)
    else:
        return 0


def write_students_information(student_list):
    number = 0
    with open("students.pickle", "wb") as f:
        for inst in student_list:
            pickle.dump(inst, f)
            number += 1
    return number


def read_groups_information():
    group_list = []
    with open("groups.pickle", "rb") as f:
        while True:
            try:
                inst = pickle.load(f)
                group_list.append(inst.specialty.name)
            except EOFError:
                break
    return set(group_list)


def read_students_information():
    student_list = []
    with open("students.pickle", "rb") as f:
        while True:
            try:
                inst = pickle.load(f)
                student_list.append(inst)
            except EOFError:
                break
    return student_list
