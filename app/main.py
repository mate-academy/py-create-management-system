from dataclasses import dataclass
import pickle


@dataclass()
class Specialty:
    name: str
    number: int


@dataclass()
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass()
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: Group) -> int:
    with open("groups.pickle", "wb") as source_file:
        pickle.dump(groups, source_file)

    max_student_numbers = 0

    for group in groups:
        if max_student_numbers < len(group.students):
            max_student_numbers = len(group.students)

    return max_student_numbers


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as source_file:
        pickle.dump(students, source_file)

        studentss = 0

        for student in students:
            studentss += 1

        return studentss


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as source_file:
        groups_list = pickle.load(source_file)

    list_of_specialty = []

    for group in groups_list:
        list_of_specialty.append(group.specialty.name)

    return set(list_of_specialty)


def read_students_information() -> list:
    with open("students.pickle", "rb") as source_file:
        students_list = pickle.load(source_file)

        students = []

        for student in students_list:
            students.append(student)

        return students
