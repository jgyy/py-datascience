"""
Bayesian Homework
"""
from math import gcd


def table():
    """
    Solves problems for table C1 and C2
    """
    rnd = lambda x: round(x * 100, 2)
    c11 = rnd(634 / 2590)
    print(f"C11) {c11}% male")
    c12 = rnd(741 / 3088)
    print(f"C11) {c12}% female")
    c13 = gcd(int(c11 * 100), int(c12 * 100))
    print(f"c13) ratio {int(c11*100/c13)}:{int(c12*100/c13)}")
    c14 = rnd(217 / 634)
    print(f"C14) {c14}% male")
    c15 = rnd(263 / 741)
    print(f"C15) {c15}% female")

    c211 = rnd(1299 / 5678)
    print(f"C211) {c211}% waiting list")
    c212 = rnd(1299 / 4304)
    print(f"C212) {c212}% waiting list")
    c22 = rnd(33 / 629)
    print(f"C22) {c22}% waiting list")
    c23 = rnd(33 / 1299)
    print(f"C23) {c23}% waiting list")


if __name__ == "__main__":
    table()
