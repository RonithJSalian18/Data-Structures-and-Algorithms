class Solution:
    def myPow(self, x: float, n: int) -> float:

        # Fast exponentiation using recursion
        def power(x, n):
            # Base case
            if n == 0:
                return 1

            # Compute x^(n//2)
            half = power(x, n // 2)

            # If n is even: x^n = (x^(n/2))²
            if n % 2 == 0:
                return half * half
            # If n is odd: x^n = (x^(n//2))² * x
            else:
                return half * half * x

        # Handle negative exponent
        if n < 0:
            return 1 / power(x, -n)

        # Compute positive exponent
        return power(x, n)