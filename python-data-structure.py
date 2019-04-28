def isTheSame(s1,s2):
    if len(s1)!= len(s2):
        return False
    else:
        flag = True
        num = 0
        s1int = list(s1)
        while num < len(s1) and flag:
            flag = s1int[num] in s2
            num = num + 1
    return flag

print(isTheSame('abcd','dcbae'))