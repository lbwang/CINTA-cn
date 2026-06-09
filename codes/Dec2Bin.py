function Dec2Bin(a)
# Input: a decimal number a;
# Output: the binary digits of a;
if a <= 1:  ＃终止条件！
    return a;
else:
    return Dec2Bin(a/2)||lsb(a) # ||是字符连接的意思.
# a/2 表示a右移了一个比特
# lsb(a)是a的最低位比特，其实就是a % 2，或者a & 1.