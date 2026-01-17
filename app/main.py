from dataclasses import dataclass
import pickle


@dataclass
class Specialty:
    def __init__(self, name: str, number: int) -> None:
        self.name = name
        self.number = number


@dataclass
class Student:
    def __init__(
            self,
            first_name: str,
            last_name: str,
            birth_date: str,
            average_mark: float,
            has_scholarship: bool,
            phone_number: int,
            address: str
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.average_mark = average_mark
        self.has_scholarship = has_scholarship
        self.phone_number = phone_number
        self.address = address
        self.birth_date = birth_date


class Group:
    def __init__(
            self,
            specialty: Specialty,
            course: int,
            students: list[Student]
    ) -> None:
        self.specialty = specialty
        self.course = course
        self.students = students


def write_groups_information(group_list: list[Group]) -> int:
    max_students = []
    with open("groups.pickle", "wb") as gr_file:
        for group in group_list:
            pickle.dump(group, gr_file)
            max_students.append(len(group.students))

    try:
        return max(max_students)
    except ValueError:
        return 0


def write_students_information(st_list: list[Student]) -> int:
    with open("students.pickle", "wb") as st_file:
        for student in st_list:
            pickle.dump(student, st_file)

    return len(st_list)


def read_groups_information() -> list:
    result = []
    with open("groups.pickle", "rb") as gr_file:
        while True:
            try:
                group = pickle.load(gr_file)
                result.append(group.specialty.name)
            except EOFError:
                break
    return list(set(result))


def read_students_information() -> list:
    st_list = []
    with open("students.pickle", "rb") as st_file:
        while True:
            try:
                student = pickle.load(st_file)
                st_list.append(student)
            except EOFError:
                break

    return st_list
