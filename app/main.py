import dataclasses
from datetime import date
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        for group in group_list:
            pickle.dump(group, pickle_file)

    if len(group_list) == 0:
        return 0

    return max([len(group.students) for group in group_list])


def write_students_information(student_list: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in student_list:
            pickle.dump(student, pickle_file)

    return len(student_list)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_file:
        specialty_dict = {}
        while True:
            try:
                specialty = pickle.load(pickle_file).specialty.name
                specialty_dict[specialty] = specialty
            except EOFError:
                break

        return specialty_dict.keys()


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        student_list = []
        while True:
            try:
                student_list.append(pickle.load(pickle_file))
            except EOFError:
                break

    return student_list
# def basic_student(
#     first_name="Ivan",
#     last_name="Ivanov",
#     birth_date=date.today(),
#     mark=87.5,
#     has_scholarship=False,
#     phone="+380999999999",
#     city="Kyiv",
# ):
#     return Student(
#         first_name, last_name, birth_date, mark, has_scholarship, phone, city
#     )
#
# groups = [
#     Group(
#         specialty=Specialty("Math and Physic", 1),
#         course=1,
#         students=[basic_student()],
#     ),
#     Group(
#         specialty=Specialty("English", 2),
#         course=2,
#         students=[
#             basic_student(),
#             basic_student(first_name="Mariia", mark=72.9),
#             basic_student(first_name="Dariia", mark=100.0),
#         ],
#     ),
#     Group(
#         specialty=Specialty("Biology", 2),
#         course=1,
#         students=[basic_student()],
#     )
# ]
#
#
# print("w", write_groups_information(groups))
# print("r", read_groups_information())
