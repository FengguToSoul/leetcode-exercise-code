class Solution:
    def romanToInt(self, s: str) -> int:
        num_need = 0
        if s[0] == 'I':
            num_need = num_need + 1
        elif s[0] == 'V':
            num_need = num_need + 5
        elif s[0] == 'X':
            num_need = num_need + 10
        elif s[0] == 'L':
            num_need = num_need + 50
        elif s[0] == 'C':
            num_need = num_need + 100
        elif s[0] == 'D':
            num_need = num_need + 500
        else:
            num_need = num_need + 1000

        for i in range(1, len(s)):
            if s[i] == 'I':
                num_need = num_need + 1
            elif s[i] == 'V':
                num_need = num_need + 5
                if s[i - 1] == 'I':
                    num_need = num_need - 2
            elif s[i] == 'X':
                num_need = num_need + 10
                if s[i - 1] == 'I':
                    num_need = num_need - 2
            elif s[i] == 'L':
                num_need = num_need + 50
                if s[i - 1] == 'X':
                    num_need = num_need - 20
            elif s[i] == 'C':
                num_need = num_need + 100
                if s[i - 1] == 'X':
                    num_need = num_need - 20
            elif s[i] == 'D':
                num_need = num_need + 500
                if s[i - 1] == 'C':
                    num_need = num_need - 200
            else:
                num_need = num_need + 1000
                if s[i - 1] == 'C':
                    num_need = num_need - 200

        return num_need
