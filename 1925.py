from math import gcd


class Solution:
    def countTriples(self, n: int) -> int:
        return self.generate_all_pythagorean_triples(n)

    def generate_all_pythagorean_triples(self, limit):
        triples = []
        m = 2
        while m * m <= limit:
            for n in range(1, m):
                if (m - n) % 2 == 1 and gcd(m, n) == 1:
                    a = m*m - n*n
                    b = 2*m*n
                    c = m*m + n*n

                    if c > limit:
                        continue

                    # primitive 三元组
                    k = 1
                    while k * c <= limit:
                        triples.append((k*a, k*b, k*c))
                        k += 1
            m += 1

        return len(triples) * 2