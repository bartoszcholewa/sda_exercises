"""
Podgląd funkcji w assemblerze
"""
from dis import dis

def compute_delta(a, b, c):
    return b ** 2 - 4 * a * c

dis(compute_delta)