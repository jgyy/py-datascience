"""
Combinatorics Exercises
"""
from math import factorial as f


def problem1_3():
    """
    Solves problem 1 to 3
    """
    ways = f(5)
    print(f"1) {ways} ways")

    num = 8
    pos = len("Facebook Messenger Instagram Twitter Reddit".split())
    var = int(f(num) / f(num - pos))
    print(f"2a) {var} Variations without repetition")
    var_repy = num ** pos
    print(f"2b) {var_repy} Variations with repetition")
    com_repn = int(f(num) / (f(pos) * f(num - pos)))
    print(f"2c) {com_repn} Combinations without repetition")
    com_repy = int(f(num + pos - 1) / (f(pos) * f(num - 1)))
    print(f"2d) {com_repy} Combinations with repetition")

    var3a = int(f(9) / f(9 - 7))
    print(f"3a) {var3a} Variations without repetition")
    var3ba = int(f(9) / f(9 - 4))
    print(f"3ba) {var3ba} Variations without repetition")
    var3bb = int(f(8) / f(8 - 4))
    print(f"3ba) {var3bb} Variations without repetition")
    var3bc = 9 ** 4
    print(f"3ba) {var3bc} Variations with repetition")
    var3ca = 9 ** 6
    print(f"3ca) {var3ca} Variations with repetition")
    var3cb = int(f(9) / f(9 - 6))
    print(f"3cb) {var3cb} Variations with repetition")
    var3d = 2 ** 7
    print(f"3d) {var3d} Variations with repetition")


def problem4_6():
    """
    Solves problems 4 to 6
    """
    per4a = f(11)
    print(f"4a) {per4a} Permutations")
    per4b = f(10)
    print(f"4b) {per4b} Permutations")
    per4c = f(3) * f(8)
    print(f"4c) {per4c} Ways")
    per4d = 10 * f(10)
    print(f"4d) {per4d} Options")

    com5aa = int(f(5) / (f(2) * f(5 - 2)))
    print(f"5aa) {com5aa} Combinations without repetition")
    com5ab = int(f(5 + 2 - 1) / (f(2) * f(5 - 1)))
    print(f"5ab) {com5ab} Combinations with repetition")
    com5b = int(f(4 + 2 - 1) / (f(2) * f(4 - 1)))
    print(f"5b) {com5b} Combinations with repetition")
    var5ea = int(f(5) / f(5 - 2))
    print(f"5ea) {var5ea} Variations without repetition")
    var5eb = 5 ** 2
    print(f"5eb) {var5eb} Variations with repetition")

    var6 = 3 * int(f(5) / f(5 - 2)) * 4 * 4 * 4 * 2 * 2 * int(f(4) / f(4 - 2)) * 3
    print(f"6) {var6} Variations")


if __name__ == "__main__":
    problem1_3()
    problem4_6()
