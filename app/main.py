from app.my_dataclasses import Student, Group, \
    Specialty  # noqa  # pylint: disable=unused-import
import pickle


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file_groups:
        for group in groups:
            pickle.dump(group, file_groups)
        file_groups.seek(0)
        if len(groups) > 0:
            return max([len(group.students) for group in groups])
        return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file_students:
        for student in students:
            pickle.dump(student, file_students)
        file_students.seek(0)
        return len(students)


def read_groups_information() -> list[Group]:
    with open("groups.pickle", "rb") as file_groups:
        groups = []
        try:
            while True:
                group = pickle.load(file_groups)
                groups.append(group)
        except EOFError:
            pass
    return list(set([group.specialty.name for group in groups]))


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file_students:
        students = []
        try:
            while True:
                student = pickle.load(file_students)
                students.append(student)
        except EOFError:
            pass
    return students
