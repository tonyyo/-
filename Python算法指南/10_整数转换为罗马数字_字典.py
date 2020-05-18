class Solution:
    def intToRoman(self, num):
        NUMS = {
            0: '',  # 必须要有0
            1: 'I',
            2: 'II',
            3: 'III',
            4: 'IV',
            5: 'V',
            6: 'VI',
            7: 'VII',
            8: 'VIII',
            9: 'IX',
        }
        ROMAN = {
            'I': ['I', 'X', 'C', 'M'],  # 个 十 百 千
            'V': ['V', 'L', 'D', '?'],  # 五 五十 五百
            'X': ['X', 'C', 'M', '?']  # 十 百 千
        }
        ans, s = [], ""
        while num != 0:
            yu = num % 10
            ans.append(yu)
            num = num // 10
        for i in range(len(ans)):
            ans[i] = NUMS[ans[i]]
            ans[i] = ans[i].replace('X', ROMAN['X'][i]).replace('I', ROMAN['I'][i]).replace('V', ROMAN['V'][i])  # X应放在前面, 因为I中包含X
            s = ans[i] + s
        return s

if __name__ == '__main__':
    solution = Solution()
    print(solution.intToRoman(99))
