from dataclasses import dataclass
import pickle


@dataclass
class Specialty:
    name: str
    number: str


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
    students: list


def write_groups_information(groups: list[Group]) -> int:
    all_student_len_list = []
    with open("groups.pickle", "wb") as file_group:
        pickle.dump(groups, file_group)
        for group in groups:
            all_student_len_list.append(len(group.students))
    if not all_student_len_list:
        return 0
    return max(all_student_len_list)


def write_students_information(students_info: list[Student]) -> None:
    with open("students.pickle", "wb") as students_file_info:
        pickle.dump(students_info, students_file_info)
    return len(students_info)


def read_groups_information() -> str:
    result = []
    with open("groups.pickle", "rb") as group_read_file:
        response = pickle.load(group_read_file)
        for group in response:
            if group.specialty.name not in result:
                result.append(group.specialty.name)
        return result


def read_students_information() -> Student:
    result = []
    with open("students.pickle", "rb") as students_read_file:
        response = pickle.load(students_read_file)
        for student in response:
            result.append(student)
        return result
