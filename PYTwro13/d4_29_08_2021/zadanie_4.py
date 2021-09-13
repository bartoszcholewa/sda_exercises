"""Task 2 - write a function (sum_all) that computes an average of grades from all lectures.

Examples of calls:
compute_average("Ania",math=5,biology=5,polish=4,physics=1,history=5)->Student Ania, grade avg: 4.0
compute_average(math=5, student_name="Basia") -> Student Basia, grade avg: 5.0
compute_average("Krysia", physics=1, history=5) -> Student Krysia, grade avg: 3.0"""


def compute_average(student_name, **kwargs) -> str:
    """
    @param student_name:
    @param kwargs:
    @return: string
    """
    return f"Student {student_name}, grade avg: {sum(kwargs.values()) / len(kwargs)}"


print(compute_average("Ania", math=5, biology=5, polish=4, physics=1, history=5))
print(compute_average(math=5, student_name="Basia"))
print(compute_average("Krysia", physics=1, history=5))
