class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        number = ""

        for i in str:
            if i.isalpha() and number == "":
                return 0
            elif i.isalpha():
                break
            elif i == " ":
                break
            elif i == ".":
                break
            elif (i == "+" or i == "-") and number == "":
                number = number + i
            elif (i == "+" or i == "-") and number != "":
                break
            elif (i == "+" or i == "-") and ("+" in number or "-" in number):
                break
            elif i.isdigit():
                number = number + i

        if number == "" or number == "+" or number == "-":
            return 0
        else:
            if int(number) > ((2**31)-1):
                return (2**31)-1
            elif int(number) < -(2**31):
                return -(2**31)
            else:
                return int(number)


