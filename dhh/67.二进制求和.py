#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a:
            return b
        if not b:
            return a
        if len(a) > len(b):
            a, b = list(b), list(a)
        else:
            a, b = list(a), list(b)

        flag = False
        result = []
        while a and b:
            t_a = a.pop()
            t_b = b.pop()
            if t_a == t_b and t_a == '1':
                if flag:
                    result.append('1')
                else:
                    result.append('0')
                    flag = True
            elif t_a == '1' or t_b == '1':
                if flag:
                    result.append('0')
                else:
                    result.append('1')
            else:
                if flag:
                    result.append('1')
                else:
                    result.append('0')
                flag = False

        while b:
            t_b = b.pop()
            if flag and t_b == '1':
                result.append('0')
            elif flag:
                result.append('1')
                flag = False
            else:
                result.append(t_b)
        if flag:
            result.append('1')
        return ''.join(result[::-1])

