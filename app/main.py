import pickle
from typing import List
from app.group import Group, Student, Specialty


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as group_file:
        max_stud = 0
        for group in groups:
            pickle.dump(group, group_file)
            if len(group.students) > max_stud:
                max_stud = len(group.students)
        return max_stud


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as student_file:
        for student in students:
            pickle.dump(student, student_file)

        return len(students)


def read_groups_information() -> set:
    out_set = set()
    with open("groups.pickle", "rb") as group_file:
        while True:
            try:
                group = pickle.load(group_file)
                out_set.add(group.specialty.name)
            except EOFError:
                break

    return out_set


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as student_file:
        out_list = []
        while True:
            try:
                student = pickle.load(student_file)
                out_list.append(student)
            except EOFError:
                break

    return out_list
