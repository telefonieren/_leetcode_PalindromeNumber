import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x > 0:
            n = int(math.log10(x)) + 1
        else:
            return False
        dec = 1
        while x > 0:
            a = x // 10 ** (n - dec)
            b = (x - a) % 10
            if b != 0:
                return False
            x = (x - a * 10 ** (n - dec)) // 10
            if x == 0:
                return True
            a = x // 10 ** (n - dec - 2)
            dec += 2
        return False


def main():
    print(Solution().isPalindrome(3510153))


if __name__ == '__main__':
    main()
