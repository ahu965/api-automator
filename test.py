import math
from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        def A(x, y):
            return 2 * x + y

        def B(x, y):
            return 2 * y + x

        x = 1
        y = 0
        for c in s:

            if c == 'A':
                x = A(x, y)
            else:
                y = B(x, y)
            print(x, y)
        return x + y


if __name__ == '__main__':
    print(Solution().calculate("AB"))
