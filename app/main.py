from datetime import datetime

import dataclasses
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


test_speciality_1 = Specialty("math", 3)
test_speciality_2 = Specialty("physics", 2)

test_students_list_1 = [
    Student("Max", "Smith", datetime.today(), 92.3, False, "0954026307", "Ugorska St"),
    Student("Jack", "Black", datetime.today(), 52.3, False, "0954026307", "Ugorska St"),
    Student("John", "Holl", datetime.today(), 32.3, False, "0954026307", "Ugorska St")
]

test_students_list_2 = [
    Student("Max", "Smith", datetime.today(), 72.3, False, "0954026307", "Ugorska St"),
    Student("Jack", "Black", datetime.today(), 50.3, False, "0954026307", "Ugorska St"),
    Student("John", "Holl", datetime.today(), 80.3, False, "0954026307", "Ugorska St"),
    Student("Barak", "Obama", datetime.today(), 92.3, False, "0954026307", "Ugorska St")
]

test_groups = [
    Group(test_speciality_1, 3, test_students_list_1),
    Group(test_speciality_2, 4, test_students_list_2)
]


def write_groups_information(group_info: list[Group]) -> int:
    with open("groups.pickle", "wb") as groups_file:
        for group in group_info:
            pickle.dump(group, groups_file)

    return_result = 0
    for group in group_info:
        if len(group.students) > return_result:
            return_result = len(group.students)

    return return_result


print(write_groups_information(test_groups))


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as student_file:
        for student in students_list:
            pickle.dump(student, student_file)

    return len(students_list)


print(write_students_information(test_students_list_1))


def read_groups_information() -> set:
    groups_list = []
    with open("groups.pickle", "rb") as groups_file:
        while True:
            try:
                groups_list.append(pickle.load(groups_file))
            except EOFError:
                break

    groups_specialties = [group.specialty.name for group in groups_list]

    return set(groups_specialties)


print(read_groups_information())


def read_students_information() -> list[Student]:
    student_list = []

    with open("students.pickle", "rb") as student_file:
        while True:
            try:
                student_list.append(pickle.load(student_file))
            except EOFError:
                break

    return student_list


print(read_students_information())
