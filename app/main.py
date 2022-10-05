from dataclasses import dataclass
import pickle


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
    phone_number: int
    address: str


def write_students_information(students_list: list) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students_list, file)

    return len(students_list)


def read_groups_information() -> list:
    try:
        with open("groups.pickle", "rb") as file:
            groups = pickle.load(file)
            students_specialty = []
        for group in groups:
            if students_specialty.count(group.specialty.name) == 0:
                students_specialty.append(group.specialty.name)
            else:
                continue
        return students_specialty
    except FileNotFoundError:
        return []


@dataclass
class Group:
    specialty: str
    course: int
    students: list


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    max_students_count = 0

    for group in groups:
        students_count = len(group.students)
        if students_count >= max_students_count:
            max_students_count = students_count

    return max_students_count


def read_students_information() -> list:
    try:
        with open("students.pickle", "rb") as file:
            students = pickle.load(file)
            students_groups = []
            for basic_student in students:
                students_groups += [
                    Student(
                        first_name=basic_student.first_name,
                        last_name=basic_student.last_name,
                        birth_date=basic_student.birth_date,
                        average_mark=basic_student.average_mark,
                        has_scholarship=basic_student.has_scholarship,
                        phone_number=basic_student.phone_number,
                        address=basic_student.address
                    )
                ]
            return students_groups
    except FileNotFoundError:
        return []
