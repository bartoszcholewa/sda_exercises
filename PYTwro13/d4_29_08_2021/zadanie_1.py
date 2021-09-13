""" PYTwro13 - Python Podstawy
Podgląd funkcji w assemblerze
"""
from dis import dis


def compute_delta(a_a, b_b, c_c):
    """
    @param a_a: some variable 1
    @param b_b: some variable 2
    @param c_c: some variable 3
    @return: float
    """
    return b_b ** 2 - 4 * a_a * c_c


dis(compute_delta)
