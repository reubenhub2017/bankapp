class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        newArry = []
        for i in range(len(address)):
            newArry.append(address[i])
        for i in range(len(newArry)):
            if newArry[i] == ".":
                newArry[i] = "[.]"
        return "".join(newArry)


new = Solution()
print(new.defangIPaddr("1.1.1.1"))
