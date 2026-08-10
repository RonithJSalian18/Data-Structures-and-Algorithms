class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = []

        s = ''
        for i in range(len(number)):
            ch = s
            if number[i] == digit:
                if i == len(number) - 1:
                    res.append(number[:i])
                elif i >= 1:
                    ch += number[i+1:]
                    res.append(ch)
                else:
                    res.append(number[i+1:])
            s += number[i]

        maxi = res[0]
        for char in res:
            if char > maxi:
                maxi = char

        return maxi
        