from dataclasses import dataclass
import pickle
from typing import List


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(student_group: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(student_group, file)
    max_students = max([len(group.students) for group in student_group])
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "ab") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information(filename: str) -> set:
    with open(filename, "rb") as file:
        content = pickle.load(file)
        specialities = set([spec.specialty.name for spec in content])
        return specialities


def read_students_information(filename: str) -> None:
    with open(filename, "rb") as file:
        content = pickle.load(file)
        return content


if __name__ == "__main__":
    # speciality
    historian = Specialty("historian", 13)
    chemistry = Specialty("chemistry", 15)

    # students
    student_1 = Student("Alex", "Black", "16.05", 8.3, True, "093", "Ukraine")
    student_2 = Student("Anne", "White", "25.03", 11.9, True, "095", "USA")

    student_3 = Student(
        "Teya", "Shevchyck", "01.01", 100, True, "000", "Zhytomyr"
    )
    student_4 = Student("Ihor", "Gray", "10.10", 10, False, "01", "Korosten")
    student_5 = Student("Eva", "Pink", "07.10", 12, True, "21", "Netherlands")

    all_students = [student_1, student_2, student_3, student_4, student_5]
    write_students_information(all_students)
    read_students_information("students.pickle")

    # students_group
    first_group = [student_1, student_2]
    second_group = [student_3, student_4, student_5]

    # group instance
    group_1 = Group(historian, 2022, first_group)
    group_2 = Group(chemistry, 2023, second_group)

    # write_groups_information([group_1, group_2])
    #
    # read_groups_information("groups.pickle")
