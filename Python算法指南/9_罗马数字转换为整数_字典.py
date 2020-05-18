class Solution:
    def romanToInt(self, s):
        ROMAN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = ROMAN[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            if ROMAN[s[i]] >= ROMAN[s[i + 1]]:
                sum += ROMAN[s[i]]
            else:
                sum -= ROMAN[s[i]]
        return sum


if __name__ == '__main__':
    solution = Solution()
    print(solution.romanToInt1("DCXXI"))