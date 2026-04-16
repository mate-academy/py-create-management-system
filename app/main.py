import pickle
from dataclasses import dataclass


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
    students: list[Student]


def write_groups_information(groups: list[Group],
                             filename: str = "groups.pickle"):
    with open(filename, 'wb') as f:
        pickle.dump(groups, f)

    if not groups:
        return 0

    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student],
                               filename: str = "students.pickle"):
    with open(filename, 'wb') as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information(filename: str = "groups.pickle"):
    all_data = []
    try:
        with open(filename, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    # Если записан список групп, объединяем списки
                    if isinstance(obj, list):
                        all_data.extend(obj)
                    else:
                        all_data.append(obj)
                except EOFError:
                    break
    except FileNotFoundError:
        return []

    # Извлекаем уникальные названия специальностей
    unique_specs = {group.specialty.name for group in all_data}
    return list(unique_specs)


def read_students_information(filename: str = "students.pickle"):
    students = []
    try:
        with open(filename, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    if isinstance(obj, list):
                        students.extend(obj)
                    else:
                        students.append(obj)
                except EOFError:
                    break
    except FileNotFoundError:
        return []

    return students
