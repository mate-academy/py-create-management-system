import pickle
from dataclasses import dataclass
from datetime import date


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list[Group]:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    return list({group.specialty.name for group in groups})


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students


if __name__ == "__main__":
    specialty = Specialty(name="Computer Science", number=101)
    students = [
        Student("John", "Doe", date(2000, 1, 1), 89.5,
                True, "123-456-7890", "123 Main St"),
        Student("Jane", "Smith", date(1999, 5, 15), 91.0,
                False, "987-654-3210", "456 Elm St"),
    ]
    group = Group(specialty=specialty, course=1, students=students)

    # Запис інформації
    max_students = write_groups_information([group])
    print(f"Max students in a group: {max_students}")

    total_students = write_students_information(students)
    print(f"Total students written: {total_students}")

    # Читання інформації
    group_names = read_groups_information()
    print(f"Group specialties: {group_names}")

    students_from_file = read_students_information()
    print(f"Students read from file: {students_from_file}")
