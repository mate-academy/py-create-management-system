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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    try:
        max_number_of_students = len(groups[0].students)
    except IndexError:
        return 0

    for group in groups:
        students = len([student for student in group.students])

        if students > max_number_of_students:
            max_number_of_students = students

    return max_number_of_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    students_count = len([student for student in students])

    return students_count


def read_groups_information() -> list[str]:
    result = []

    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

    for group in groups:
        if group.specialty.name not in result:
            result.append(group.specialty.name)

    return result


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

    return students
