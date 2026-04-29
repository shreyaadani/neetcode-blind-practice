class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]
        if len(s) > 12:
            return res

        def  check(num):
            return len(num) == 1 or (int(num)< 256 and num[0]!="0")

        def add(s1,s2,s3,s4):
            if s1 + s2 + s3 + s4 != len(s):
                return

            num1 = s[:s1]
            num2 = s[s1:s1+s2]
            num3 = s[s1+s2:s1+s2+s3]
            num4 = s[s1+s2+s3:]  
            if check(num1) and check(num2) and check(num3) and check(num4):
                res.append(num1 + "."+num2 + "."+ num3 + "."+ num4)         

        for seg1 in range(1,4):
            for seg2 in range(1,4):
                for seg3 in range(1,4):
                    for seg4 in range(1,4):
                        add(seg1,seg2,seg3,seg4)

        return res                