# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def pivotIndex(nums: list[int]) -> int:
    print(f"nums = {nums}")
    summation = 0
    leftSummation = 0
    for num in nums:
        summation += num

    for index in range(len(nums)):
        if (index == 0 or index == (len(nums)-1)) and (summation - nums[index]) == 0:
            return index
        else:
            leftSummation = leftSummation + nums[index-1] if index > 0 else 0
            print(f"leftSummation = {leftSummation}, pivot number = {nums[index]}, rightSummation = {summation - nums[index] - leftSummation}")
            if summation - nums[index] - leftSummation == leftSummation:
                return index
    return -1


def isIsomorphic(s: str, t: str) -> bool:
    print(f"Origin -- s={s}, t={t}")
    for index, alpha in enumerate(s):
        print(f"index={index}, alpha={alpha}, t[index] = {t[index]}")
        t = t.replace(t[index], alpha)
    print(f"After replace -- s={s}, t={t}")

    if t == s :
        return True
    else:
        return False






if __name__ == '__main__':
    # print("Result = {}".format(pivotIndex([1, 7, 3, 6, 5, 6])))
    # print("Result = {}".format(pivotIndex([1,2,3])))
    # print("Result = {}".format(pivotIndex([-1,-1,-1,-1,-1,0])))
    # print("Result = {}".format(pivotIndex([1, 7, 3, 6, 5, 6])))
    print(f"Result = {isIsomorphic('egg', 'add')}")
    print(f"Result = {isIsomorphic('foo', 'bar')}")
    print(f"Result = {isIsomorphic('paper', 'title')}")


# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/





