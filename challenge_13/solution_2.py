"""
Filter Students Older Than a Specified Age Limit
================================================
Author: Udit Kumar Chatterjee
Email: quantumudit@gmail.com
================================================

This script defines a function, filter_students_older_than_limit, which filters a list 
of student data to include only students less than a specified age limit.
"""


def filter_students_older_than_limit(student_data: list, age_limit: int):
    """
    Filters a list of student data to include only students older than a specified age limit.

    Args:
        student_data (list): A list of tuples or lists containing student information.
                            Each student data item should have at least three elements:
                            (name: str, age: int, other_info: any)
        age_limit (int): The minimum age for students to be included in the filtered list.

    Returns:
        list: A filtered list containing student data for students older than the age limit.
            Each item in the filtered list has the same format as the input data.

    Raises:
        ValueError: If the data format is not a tuple or a list with at least three elements,
                    or if the age is not an integer.
    """
    filtered_data = []

    for student_info in student_data:
        if isinstance(student_info, (tuple, list)) and len(student_info) == 3:
            _, age, _ = student_info

            if isinstance(age, int):
                if age < age_limit:
                    filtered_data.append(student_info)
                else:
                    pass
            else:
                raise ValueError(
                    f"Student age should be an integer value: {student_info}")
        else:
            raise ValueError(
                f"The data format must be a tuple or a list with three elements: {student_info}")

    return filtered_data


if __name__ == '__main__':
    student_dataset = [
        ("John", 13, "Grade 10"),
        ("Emily", 14, "Grade 9"),
        ("Sam", 16, "Grade 11")
    ]

    result = filter_students_older_than_limit(student_dataset, 15)
    print(result)
