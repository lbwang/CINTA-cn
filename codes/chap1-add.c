//输入: 两个整数a和b
//输出: a与b的和
int add(int a, int b) {
    if (b == 0) return a;
    return add(a ^ b, (b & a) << 1);
}