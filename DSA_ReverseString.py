from typing import List


def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    print(f"s = {s}")
    result = []
    for index in range(len(s) - 1, -1, -1):
        result.append(s[index])
    print(f"result = {result}")
    s = result
    print(f"s = {s}")


reverseString(['h', 'e', 'l', 'l', 'o'])
