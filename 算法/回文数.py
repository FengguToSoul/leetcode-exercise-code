class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        flag = 0
        for i in range(len(x_str)//2):
            if x_str[i] == x_str[len(x_str)-1-i]:
                continue
            else:
                flag = 1
                break
        if flag == 0:
            return bool(1)
        else:
            return bool(0)
