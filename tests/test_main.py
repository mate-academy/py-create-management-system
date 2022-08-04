import pytest
import os
import unittest.mock

from datetime import date

import app.main
from app.main import (
    Specialty,
    Student,
    Group,
    write_groups_information,
    write_students_information,
    read_groups_information,
    read_students_information,
)


def remove_created_test_file(path):
    if os.path.exists(path):
        os.remove(path)


@pytest.mark.parametrize("attribute", ["name", "number"])
def test_specialty_instance(attribute):
    specialty = Specialty("Math and Physic", 1)
    assert hasattr(
        specialty, attribute
    ), f"Specialty instance should have attribute '{attribute}'"


@pytest.mark.parametrize("attribute,attr_type", [("name", str), ("number", int)])
def test_specialty_instance_type(attribute, attr_type):
    specialty = Specialty("Math and Physic", 1)
    assert isinstance(
        getattr(specialty, attribute), attr_type
    ), f"Specialty instance attribute '{attribute}' should be {attr_type}"


@pytest.mark.parametrize(
    "attribute",
    [
        "first_name",
        "last_name",
        "birth_date",
        "average_mark",
        "has_scholarship",
        "phone_number",
        "address",
    ],
)
def test_student_instance(attribute):
    student = Student(
        "Ivan", "Ivanov", date.today(), 87.5, True, "+380999999999", "Kyiv"
    )
    assert hasattr(
        student, attribute
    ), f"Student instance should have attribute '{attribute}'"


@pytest.mark.parametrize(
    "attribute,attr_type",
    [
        ("first_name", str),
        ("last_name", str),
        ("birth_date", date),
        ("average_mark", float),
        ("has_scholarship", bool),
        ("phone_number", str),
        ("address", str),
    ],
)
def test_student_instance_type(attribute, attr_type):
    student = Student(
        "Ivan", "Ivanov", date.today(), 87.5, True, "+380999999999", "Kyiv"
    )
    assert isinstance(
        getattr(student, attribute), attr_type
    ), f"Specialty instance attribute '{attribute}' should be {attr_type}"


@pytest.mark.parametrize(
    "attribute",
    [
        "specialty",
        "course",
        "students",
    ],
)
def test_group_instance(attribute):
    specialty = Specialty("Math and Physic", 1)
    student1 = Student(
        "Ivan", "Ivanov", date.today(), 87.5, True, "+380999999999", "Kyiv"
    )
    student2 = Student(
        "Mariia", "Koval", date.today(), 87.5, True, "+380999999999", "Kyiv"
    )

    group = Group(specialty, 1, [student1, student2])

    assert hasattr(
        group, attribute
    ), f"Group instance should have attribute '{attribute}'"


@pytest.mark.parametrize(
    "attribute,attr_type",
    [
        ("specialty", Specialty),
        ("course", int),
        ("students", list),
    ],
)
def test_group_instance_type(attribute, attr_type):
    specialty = Specialty("Math and Physic", 1)
    student1 = Student(
        "Ivan", "Ivanov", date.today(), 87.5, True, "+380999999999", "Kyiv"
    )
    student2 = Student(
        "Mariia", "Koval", date.today(), 87.5, True, "+380999999999", "Kyiv"
    )

    group = Group(specialty, 1, [student1, student2])

    assert isinstance(
        getattr(group, attribute), attr_type
    ), f"Specialty instance attribute '{attribute}' should be {attr_type}"


@pytest.mark.parametrize(
    "kwargs,result",
    [
        ([Group(specialty=Specialty("Math and Physic", 1), course=1, students=[])], 0),
        (
            [
                Group(
                    specialty=Specialty("Biology", 2),
                    course=1,
                    students=[
                        Student(
                            "Mariia",
                            "Koval",
                            date.today(),
                            87.5,
                            True,
                            "+380999999999",
                            "Kyiv",
                        )
                    ],
                )
            ],
            1,
        ),
        (
            [
                Group(
                    specialty=Specialty("English", 2),
                    course=2,
                    students=[
                        Student(
                            "Ivan",
                            "Ivanov",
                            date.today(),
                            87.5,
                            True,
                            "+380999999999",
                            "Kyiv",
                        ),
                        Student(
                            "Mariia",
                            "Koval",
                            date.today(),
                            87.5,
                            True,
                            "+380999999999",
                            "Kyiv",
                        ),
                        Student(
                            "Ivan",
                            "Ivanov",
                            date.today(),
                            26.2,
                            True,
                            "+380999999999",
                            "Kyiv",
                        ),
                    ],
                ),
                Group(
                    specialty=Specialty("Biology", 2),
                    course=1,
                    students=[
                        Student(
                            "Mariia",
                            "Koval",
                            date.today(),
                            87.5,
                            True,
                            "+380999999999",
                            "Kyiv",
                        )
                    ],
                ),
            ],
            3,
        ),
    ],
)
def test_write_groups_information(kwargs, result):
    max_students_count = write_groups_information(kwargs)
    assert max_students_count == result, (
        f"Function write_groups_information must return a number of max students quantity in the group, "
        f"expected: {result}, but actual returned {max_students_count}"
    )


@pytest.mark.parametrize(
    "group",
    [
        Group(specialty=Specialty("Math and Physic", 1), course=1, students=[]),
        Group(
            specialty=Specialty("Biology", 2),
            course=1,
            students=[
                Student(
                    "Mariia", "Koval", date.today(), 87.5, True, "+380999999999", "Kyiv"
                )
            ],
        ),
    ],
)
def test_write_groups_information_created_file(group):

    open_mock = unittest.mock.mock_open()
    with unittest.mock.patch("app.main.open", open_mock, create=True):
        app.main.write_groups_information([group])

    remove_created_test_file("groups.pickle")

    open_mock.assert_called_with("groups.pickle", "wb")


@pytest.mark.parametrize(
    "students,result",
    [
        ([], 0),
        (
            [
                Student(
                    "Mariia", "Koval", date.today(), 87.5, True, "+380999999999", "Kyiv"
                )
            ],
            1,
        ),
        (
            [
                Student(
                    "Ivan", "Ivanov", date.today(), 87.5, True, "+380999999999", "Kyiv"
                ),
                Student(
                    "Mariia", "Koval", date.today(), 87.5, True, "+380999999999", "Kyiv"
                ),
                Student(
                    "Ivan", "Ivanov", date.today(), 26.2, True, "+380999999999", "Kyiv"
                ),
            ],
            3,
        ),
    ],
)
def test_write_students_information(students, result):
    students_count = write_students_information(students)
    assert students_count == result, (
        f"Function write_students_information must return a number of students, "
        f"expected: {result} but actual returned: {students_count}"
    )


@pytest.mark.parametrize(
    "students",
    [
        [],
        [Student("Mariia", "Koval", date.today(), 87.5, True, "+380999999999", "Kyiv")],
        [
            Student(
                "Ivan", "Ivanov", date.today(), 87.5, True, "+380999999999", "Kyiv"
            ),
            Student(
                "Mariia", "Koval", date.today(), 87.5, True, "+380999999999", "Kyiv"
            ),
            Student(
                "Ivan", "Ivanov", date.today(), 26.2, True, "+380999999999", "Kyiv"
            ),
        ],
    ],
)
def test_write_students_information_created_file(students):
    open_mock = unittest.mock.mock_open()

    with unittest.mock.patch("app.main.open", open_mock, create=True):
        app.main.write_students_information(students)

    remove_created_test_file("students.pickle")

    open_mock.assert_called_with("students.pickle", "wb")


@pytest.mark.parametrize(
    "groups,result",
    [
        ([], []),
        (
            [Group(specialty=Specialty("Math and Physic", 1), course=1, students=[])],
            ["Math and Physic"],
        ),
        (
            [
                Group(
                    specialty=Specialty("Biology", 2),
                    course=1,
                    students=[
                        Student(
                            "Mariia",
                            "Koval",
                            date.today(),
                            87.5,
                            True,
                            "+380999999999",
                            "Kyiv",
                        )
                    ],
                ),
                Group(
                    specialty=Specialty("English", 1),
                    course=2,
                    students=[
                        Student(
                            "Ivan",
                            "Ivanov",
                            date.today(),
                            87.5,
                            True,
                            "+380999999999",
                            "Kyiv",
                        ),
                        Student(
                            "Mariia",
                            "Koval",
                            date.today(),
                            87.5,
                            True,
                            "+380999999999",
                            "Kyiv",
                        ),
                        Student(
                            "Ivan",
                            "Ivanov",
                            date.today(),
                            26.2,
                            True,
                            "+380999999999",
                            "Kyiv",
                        ),
                    ],
                ),
            ],
            ["Biology", "English"],
        ),
        (
            [
                Group(
                    specialty=Specialty("English", 1),
                    course=2,
                    students=[
                        Student(
                            "Ivan",
                            "Ivanov",
                            date.today(),
                            87.5,
                            True,
                            "+380999999999",
                            "Kyiv",
                        ),
                        Student(
                            "Mariia",
                            "Koval",
                            date.today(),
                            87.5,
                            True,
                            "+380999999999",
                            "Kyiv",
                        ),
                        Student(
                            "Ivan",
                            "Ivanov",
                            date.today(),
                            26.2,
                            True,
                            "+380999999999",
                            "Kyiv",
                        ),
                    ],
                ),
                Group(
                    specialty=Specialty("English", 2),
                    course=1,
                    students=[
                        Student(
                            "Mariia",
                            "Koval",
                            date.today(),
                            87.5,
                            True,
                            "+380999999999",
                            "Kyiv",
                        )
                    ],
                ),
            ],
            ["English"],
        ),
    ],
)
def test_read_groups_information(groups, result):
    write_groups_information(groups)
    specialties = read_groups_information()

    remove_created_test_file("groups.pickle")

    assert sorted(specialties) == sorted(result), (
        f"Function read_groups_information must return a list of all specialties names, "
        f"expected: {result}, but actual returned: {specialties}"
    )


@pytest.mark.parametrize(
    "students",
    [
        [],
        [Student("Mariia", "Koval", date.today(), 87.5, True, "+380999999999", "Kyiv")],
        [
            Student(
                "Ivan", "Ivanov", date.today(), 87.5, True, "+380999999999", "Kyiv"
            ),
            Student(
                "Mariia", "Koval", date.today(), 87.5, True, "+380999999999", "Kyiv"
            ),
            Student(
                "Ivan", "Ivanov", date.today(), 26.2, True, "+380999999999", "Kyiv"
            ),
        ],
    ],
)
def test_read_students_information(students):
    write_students_information(students)
    students_list = read_students_information()

    remove_created_test_file("students.pickle")

    assert students_list == students, (
        f"Function read_students_information must return a list of all students, "
        f"expected: {students}, but actual returned: {students_list} "
    )
