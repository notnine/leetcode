import math

def is_smart_number(num):
    val = int(math.sqrt(num))
    if val * val == num: # a number is a smart number iff it is a perfect square
        return True
    return False

for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")
