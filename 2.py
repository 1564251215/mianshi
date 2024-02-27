def fun(str, k):
    new_str = ""
    count = {}
    for i, ch in enumerate(str):
        if ch in count and i - count[ch] <= k:
            new_str += "-"
        else:
            new_str += ch
        count[ch] = i
    return new_str


str=input()
k=input()
k=int(k)

out=fun(str,k)
print("Input:", str)
print("Output:", out)

#输入：
# abcdefaxcqwertba
# 10
#输出：
# Input: abcdefaxcqwertba
# Output: abcdef-x-qw-rtb-

# 输入
# abcdefaxc
# 10
# 输出
# Input: abcdefaxc
#Output: abcdef-x-