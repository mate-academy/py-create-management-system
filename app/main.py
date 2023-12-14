import dataclasses
import pickle
from datetime import datetime


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


# list1 = [
#    Group(
#          specialty=Specialty("English", 2),
#          course=2,
#          students=[
#          Student("Pavol", "Iov", datetime.now(), 45.1,
#                  True, "+380", "Ukraine"),
#          Student("Pavol2", "Iov", datetime.now(), 45.1,
#                  True, "+380", "Ukraine"),
#          Student("Pavol3", "Iov", datetime.now(), 45.1,
#                  True, "+380", "Ukraine"),
#                     ],
#                 ),
#     Group(
#           specialty=Specialty("Biology", 2),
#           course=1,
#           students=[Student("Olga", "Iov", datetime.now(),
#           45.1, True, "+380", "Ukraine")],
#                 ),
#             ]


# list2 = [
#    Student("Pavol", "Iov", datetime.now(), 45.1, True, "+380", "Ukraine"),
#    Student("Pavol2", "Iov", datetime.now(), 45.1, True, "+380", "Ukraine"),
#    Student("Pavol3", "Iov", datetime.now(), 45.1, True, "+380", "Ukraine"),
#         ]


def write_groups_information(list_inst: list) -> int:
    with open("groups.pickle", "wb") as destination_file:
        count_students = 0
        for group in list_inst:
            if len(group.students) > count_students:
                count_students = len(group.students)
        pickle.dump(list_inst, destination_file)
        return count_students


def read_groups_information(file_name: str = "groups.pickle") -> list:
    specialties = []
    with open(file_name, "rb") as source_file:
        groups = pickle.load(source_file)
        for group in groups:
            if group.specialty.name not in specialties:
                specialties.append(group.specialty.name)

        return specialties


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as destination_file:
        pickle.dump(students, destination_file)
        return len(students)


def read_students_information(file_name: str = "students.pickle") -> list:

    with open(file_name, "rb") as source_file:
        students = pickle.load(source_file)

    return students


# print(write_groups_information(list1))
# print(read_groups_information("groups.pickle"))
# print(write_students_information(list2))
# print(read_students_information("students.pickle"))
