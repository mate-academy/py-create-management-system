import pickle


class Specialty:
    def __init__(self, name: str, number: int) -> None:
        self.name = name
        self.number = number

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Specialty):
            return False
        return self.name == other.name and self.number == other.number


class Student:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        birth_date: str,
        average_mark: float,
        has_scholarship: bool,
        phone_number: str,
        address: str,
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.average_mark = average_mark
        self.has_scholarship = has_scholarship
        self.phone_number = phone_number
        self.address = address

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return False
        return (
            self.first_name == other.first_name
            and self.last_name == other.last_name
            and self.average_mark == other.average_mark
        )


class Group:
    def __init__(
        self, specialty: Specialty, course: int, students: list[Student]
    ) -> None:
        self.specialty = specialty
        self.course = course
        self.students = students

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Group):
            return False
        return (
            self.specialty == other.specialty
            and self.course == other.course
            and self.students == other.students
        )


def write_groups_information(groups: list[Group]) -> int:
    filename = "groups.pickle"
    with open(filename, "wb") as f:
        pickle.dump(groups, f)

    if not groups:
        return 0

    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    filename = "students.pickle"
    with open(filename, "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> list[str]:
    groups_data = []
    filename = "groups.pickle"
    try:
        with open(filename, "rb") as f:
            while True:
                try:
                    obj = pickle.load(f)
                    if isinstance(obj, list):
                        groups_data.extend(obj)
                    else:
                        groups_data.append(obj)
                except EOFError:
                    break
    except FileNotFoundError:
        return []

    return list({group.specialty.name for group in groups_data})


def read_students_information() -> list[Student]:
    students = []
    filename = "students.pickle"
    try:
        with open(filename, "rb") as f:
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
