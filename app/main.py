import pickle

from dataclasses import dataclass
from datetime import datetime


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
    course: int
    students: list[Student]


def write_groups_information(groups_list: list[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as file:
        for group in groups_list:
            pickle.dump(group, file)
            if len(group.students) > max_students:
                max_students = len(group.students)
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for each in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information():
    unique_specialties = []
    # with open("groups.pickle", "rb") as file:
    #     data = pickle.load(file)
    #     re_dara = pickle.loads(data)
    # print(re_dara)
    # print(data) while not EOFError
    pass

def read_students_information():
    pass


# birth_date=datetime(2005, 5, 15)
# print(birth_date)
# print(type(birth_date))

# # Specialty
# specialty = Specialty(name="Math", number=101)
# # Student
# student = Student(
#     first_name="Ivan",
#     last_name="Petrov",
#     birth_date=datetime(2005, 5, 15),
#     average_mark=85.5,
#     has_scholarship=True,
#     phone_number="+380501234567",
#     address="Kyiv, Shevchenko St 10"
# )
# # Group
# group1 = Group(
#     specialty=specialty,
#     course=2,
#     students=[]
# )
# group2 = Group(
#     specialty=specialty,
#     course=2,
#     students=[student, student]
# )
# group3 = Group(
#     specialty=specialty,
#     course=2,
#     students=[student, student, student]
# )
# group_list = [group1, group2, group3]
#
# print(write_groups_information(group_list))
# print(read_groups_information())