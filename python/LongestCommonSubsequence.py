#Rec approach

def lcs_rec(str1, str2, res):
    if len(str1) == 0 or len(str2) == 0:
        return res
    if str1[-1] == str2[-1]:
        return res+str1[-1]
    res_1 = lcs_rec(str1[:-1], str2, res)
    res_2 = lcs_rec(str1, str2[:-1], res)
    if len(res_1) < len(res_2):
        res = res+res_2
    else:
        res = res+res_1
    return res

print(lcs_rec("acbaed", "abcadf", ""))

