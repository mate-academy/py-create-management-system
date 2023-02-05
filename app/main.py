# write your code here
import dataclasses
import pickle
from typing import List


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: int
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(group_info: List[Group]) -> int:
    with open("groups.pickle", "wb") as group_pickle:
        pickle.dump(group_info, group_pickle)

    for group in group_info:
        result = 0
        if len(group.students) > result:
            return len(group.students)
        return result


def write_students_information(student_info: List[Student]) -> int:
    with open("students.pickle", "wb") as student_pickle:
        pickle.dump(student_info, student_pickle)
    return len(student_info)


def read_groups_information() -> list:
    specialities_list = []
    with open("groups.pickle", "rb") as read_pickle:
        group_list = pickle.load(read_pickle)
    for group in group_list:
        if group.specialty.name not in specialities_list:
            specialities_list.append(group.specialty.name)
    return specialities_list


def read_students_information() -> list:
    name_of_student_list = []
    with open("students.pickle", "rb") as read_pickle:
        students_list = pickle.load(read_pickle)
    for student in students_list:
        if student not in name_of_student_list:
            name_of_student_list.append(student)
    return name_of_student_list
