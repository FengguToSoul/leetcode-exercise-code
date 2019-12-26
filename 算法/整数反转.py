class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        num_need = ''
        if x_str[0] == '-':
            num_need += '-'
            for i in range(len(x_str)-1):
                num_need += x_str[len(x_str)-1-i]
        else:
            for i in range(len(x_str)):
                num_need += x_str[len(x_str)-1-i]
        num_need = int(num_need)
        if num_need < -(2**31) or num_need > (2**31-1):
            return 0
        else:
            return num_need
