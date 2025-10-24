"""
Lab 1: Logic, Quantifiers, and Number Operations
Student Name: __________________
Student ID: ___________________
Filename must be lab1_<STUDENTID>.py

------------------------------------------------------------
LEARNING NOTE: About "Callable" and "Iterable" type hints
------------------------------------------------------------

1. Callable[[int], bool]
   - Means “a function you can call with an int, that returns a bool.”
   - Example:
         def is_even(x): return x % 2 == 0
     Here `is_even` is a *callable* because we can call it like is_even(4).

   - You can also use short inline functions called *lambdas*:
         check_existential(lambda x: x < 0, [1, 2, 3])
     This means “check if there exists an x in [1,2,3] where x < 0.”

2. Iterable[int]
   - Means “any collection of integers you can loop over.”
   - Lists, ranges, and even tuples are all *iterables*:
         [1, 2, 3]        ✅ Iterable
         range(5)         ✅ Iterable
         (1, 2, 3)        ✅ Iterable
         42               ❌ Not iterable (it’s just a number)

   - In practice: if you can use “for x in something:” — then it’s iterable.
   - Example:
         for x in [1, 2, 3]:
             print(x)

💡 Type hints (like Callable and Iterable) DO NOT change how your code runs.
They just help others understand what kind of data each function expects.
------------------------------------------------------------
"""

from typing import Callable, Iterable

# -------------------------------------------------------
# QUANTIFIER SIMULATION
# -------------------------------------------------------

def check_universal(predicate: Callable[[int], bool], domain: Iterable[int]) -> bool:
    """
    Simulate ∀x in domain: predicate(x)
    Returns True if predicate(x) is True for all x in the domain.
    """
    # TODO: implement this function
    pass


def check_existential(predicate: Callable[[int], bool], domain: Iterable[int]) -> bool:
    """
    Simulate ∃x in domain: predicate(x)
    Returns True if there exists an x in the domain for which predicate(x) is True.
    """
    # TODO: implement this function
    pass


def nested_quantifiers(predicate: Callable[[int, int], bool],
                       domain_x: Iterable[int],
                       domain_y: Iterable[int]) -> dict:
    """
    Evaluate all four nested quantifier combinations on a 2-variable predicate P(x, y):
      ∀x∀y P(x,y)
      ∀x∃y P(x,y)
      ∃x∀y P(x,y)
      ∃x∃y P(x,y)
    Returns a dictionary with boolean results.
    """
    # TODO: implement this function
    pass


# -------------------------------------------------------
# NUMBER THEORY FUNCTIONS
# -------------------------------------------------------

def is_divisible(a: int, b: int) -> bool:
    """
    Return True if b divides a (a = b*k for some integer k, b ≠ 0).
    """
    # TODO: implement this function
    pass


def gcd(a: int, b: int) -> int:
    """
    Compute gcd(a, b) using the Euclidean algorithm.
    """
    # TODO: implement this function
    pass


def mod_equiv(a: int, b: int, m: int) -> bool:
    """
    Return True if a ≡ b (mod m).
    """
    # TODO: implement this function
    pass


def mod_exp(base: int, exp: int, mod: int) -> int:
    """
    Fast modular exponentiation: base^exp % mod.
    """
    # TODO: implement this function
    pass


def is_prime(n: int) -> bool:
    """
    Simple primality test (trial division).
    """
    # TODO: implement this function
    pass


# -------------------------------------------------------
# SAMPLE RUN / DEMO
# -------------------------------------------------------

if __name__ == "__main__":
    print("----------------------------------------------")
    print("Lab 1: Logic, Quantifiers, and Number Operations")
    print("Student: Your Name Here   ID: YourIDHere")
    print("----------------------------------------------\n")

    # -------------------------------
    print("[1] Quantifier Simulation:")
    domain = [1, 2, 3, 4, 5]
    print(f"Domain = {domain}")

    # Using a normal named function
    def is_less_than_10(x): return x < 10

    # Using both styles: function and lambda
    print("∀x (x < 10)?  ", check_universal(is_less_than_10, domain))
    print("∃x (x == 3)?  ", check_existential(lambda x: x == 3, domain))
    print("∃x (x < 0)?   ", check_existential(lambda x: x < 0, domain))
    print("----------------------------------------------\n")

    # -------------------------------
    print("[2] Nested Quantifiers Examples:")
    domain_x = range(1, 4)  # note: range is also iterable
    domain_y = [1, 2, 3]

    def P(x, y): return x < y
    results = nested_quantifiers(P, domain_x, domain_y)
    print("Predicate: P(x, y) = (x < y)")
    print(results)

    def Q(x, y): return (x + y) % 2 == 0
    results = nested_quantifiers(Q, domain_x, domain_y)
    print("\nPredicate: Q(x, y) = ((x + y) % 2 == 0)")
    print(results)
    print("----------------------------------------------\n")

    # -------------------------------
    print("[3] Number Theory & Arithmetic:")
    print("is_divisible(12, 4) →", is_divisible(12, 4))
    print("gcd(24, 36) →", gcd(24, 36))
    print("mod_equiv(17, 5, 6) →", mod_equiv(17, 5, 6))
    print("mod_equiv(24, 14, 6) →", mod_equiv(24, 14, 6))
    print("mod_exp(3, 4, 5) →", mod_exp(3, 4, 5))
    print("----------------------------------------------\n")

    # -------------------------------
    print("[4] Further Exploration:")
    print("is_prime(17) →", is_prime(17))
    print("is_prime(15) →", is_prime(15))
    print("----------------------------------------------")
    print("End of demo. Use 'pytest -q' to run tests.")
    print("----------------------------------------------")
