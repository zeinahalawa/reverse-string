    def reverseString(self, s):
        x = len(s)
        y= len(s)-1
        mid = x //2
        for counter in range(mid):
            temp = s[counter]
            s[counter] = s[y-counter]
            s[y-counter]=temp
           
