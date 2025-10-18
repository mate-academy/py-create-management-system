from dataclasses import dataclass
import pickle
import datetime


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
    speciality: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_input: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        max_students = 0
        for group in group_input:
            print(group.students)
            temp_max_students = len(group.students)
            if temp_max_students > max_students:
                max_students = temp_max_students
        pickle.dump(group_input, pickle_file)
        return max_students


def write_students_information(students_list: list) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students_list, pickle_file)
    return len(students_list)


def read_groups_information() -> pickle:
    with open("groups.pickle", "rb") as read_groups:
        read = pickle.load(read_groups)
        not_repeated_spec = []
        for group in read:
            if group.speciality.name not in not_repeated_spec:
                not_repeated_spec.append(group.speciality.name)
    return not_repeated_spec


def read_students_information() -> list:
    with open("students.pickle", "rb") as read_students:
        read = pickle.load(read_students)
    return read
