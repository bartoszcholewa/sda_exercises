"""Task 3 - write a function (sum_all) that computes an average of grades from all lectures,
but names of subjects can be unknown.

Examples of calls:
compute_average_elastic("Ania", 1, 5, math=5, biology=5, polish=4) -> Student Ania, grade avg: 4.0
compute_average_elastic("Basia", 5, 4, 3) -> Student Basia, grade avg: 4.0
compute_average_elastic("Krysia", 1, biology=5, polish=4) -> Student Krysia, grade avg: 3.3333333333333335"""
from statistics import mean


def compute_average_elastic(student_name, *args, **kwargs) -> str:
    avg_grades = (sum(args) + sum(kwargs.values())) / (len(args) + len(kwargs))
    return f"Student {student_name}, grade avg: {avg_grades}"


print(compute_average_elastic("Ania", 1, 5, math=5, biology=5, polish=4))
print(compute_average_elastic("Basia", 5, 4, 3))
print(compute_average_elastic("Krysia", 1, biology=5, polish=4))
