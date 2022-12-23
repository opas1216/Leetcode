# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Leetcode #724
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

# Leetcode #205
def isIsomorphic(s: str, t: str) -> bool:
    print(f"s={s}, t={t}")
    # collect_dict_a, collect_dict_b = {}, {}
    # index_to_alpha_dict = {}
    # for index, alpha in enumerate(s):
    #     if alpha not in collect_dict_a:
    #         collect_dict_a[alpha] = [index]
    #     else:
    #         collect_dict_a[alpha].append(index)
    #
    # for index, alpha in enumerate(t):
    #     if alpha not in collect_dict_b:
    #         collect_dict_b[alpha] = [index]
    #     else:
    #         collect_dict_b[alpha].append(index)
    #     index_to_alpha_dict[index] = alpha
    #
    # if len(collect_dict_a) == len(collect_dict_b):
    #     for key, value in collect_dict_a.items():
    #         print(f"Key = {key}, value = {value}, len of value = {len(value)}")
    #         if len(value)>1:
    #             for index, element in enumerate(value):
    #                 print(f"Index and Element of Enumerate(value) = {index} & {element}")
    #                 if index == 0:
    #                     compare_alpha = index_to_alpha_dict[element]
    #                 else:
    #                     print(f"compare_alpha = {compare_alpha}, index_to_alpha_dict[index] = {index_to_alpha_dict[element]}")
    #                     if compare_alpha != index_to_alpha_dict[element]:
    #                         return False
    #     return True
    # else:
    #     print(f"The amount of distinct characters from s & t is different.")
    #     return False

    character_list_s, character_list_t = [], []
    character_dict = {}
    # Can use Set to replace the below purpose.
    # for character in s:
    #     if character not in character_list_s:
    #         character_list_s.append(character)
    # for character in t:
    #     if character not in character_list_t:
    #         character_list_t.append(character)
    # if len(s) != len(t) or len(character_list_s) != len(character_list_t): return False

    if len(s) != len(t) or len(set(s)) != len(set(t)): return False

    for index, character in enumerate(s):
        if character not in character_dict:
            character_dict[character] = t[index]
        else:
            if character_dict[character] != t[index]: return False
    return True

# Leetcode #392
def isSubsequence(s: str, t: str) -> bool:
    ############# My Solution
    # current_index = 0
    # for index, character in enumerate(s):
    #     character_match = False
    #     for target_index in range(current_index, len(t)):
    #         if character == t[target_index]:
    #             print(f"character from s {character} is equal to target character {t[target_index]} from t at index {target_index}")
    #             current_index = target_index + 1
    #             character_match = True
    #             break
    #         if target_index == len(t) and index < len(s)-1:
    #             print(f"Target index {target_index} reach the length of t {len(t)}, but the major index is at {index}")
    #             return False
    #     if character_match == False: return False
    # return True

    #Better way from leetcode
    index = 0
    for character in s:
        if character in t[index:]:
            t = t[t[index:].index(character)+1:]
        else:
            return False
    return True

# Leetcode #21
# Merge Two Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         result = ListNode(self)
#         if list1.val <= list2.val:
#             result.val = list1.val
#         else:
#             result.val = list2.val
#         while(list1.next!= None or list2.next!= None):
#             print(f"list1 value = {list1.val}")
#             if list1.val <= list2.val:
#                 result.next = list1.next
#                 list1 = list1.next
#             else:
#                 result.next = list2.next
#                 list2 = list2.next
#         print(result)
    # Better way #1 from Leetcode
    # if list1 is None:
    #     print(list2)
    #     return list2
    # elif list2 is None:
    #     print(list1)
    #     return list1
    # elif list1.val < list2.val:
    #     list1.next = self.mergeTwoLists(list1.next, list2)
    #     print(list1)
    #     return list1
    # else:
    #     list2.next = self.mergeTwoLists(list1, list2.next)
    #     print(list2)
    #     return list2
    #
    #
    # Better way #2 from Leetcode
    # dummy = cur = ListNode(0)
    # print(f"list1 and list2 = {list1 and list2}")
    # print(f"list1 = {list1}, list2 = {list2}")
    # while list1 and list2:
    #     print(f"list1.val = {list1.val}, list2.val = {list2.val}")
    #     print(f"""cur = {cur}
    #     dummy = {dummy}""")
    #     if list1.val < list2.val:
    #         cur.next = list1
    #         list1 = list1.next
    #     else:
    #         cur.next = list2
    #         list2 = list2.next
    #     print(f"""cur = {cur}
    #     dummy = {dummy}""")
    #     cur = cur.next
    #     print(f"""After assign next to cur
    #     cur = {cur}
    #     dummy = {dummy}""")
    #     # print(f"dummy = {dummy}")
    #     print("")
    # cur.next = list1 or list2
    # return dummy.next

# 206. Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

def find_length(nums, k):
    left = curr = ans = 0
    for right in range(len(nums)):
        print(f"right = {right}, nums[{right}] = {nums[right]}")
        curr += nums[right]
        print(f"curr = {curr}")
        while curr > k:
            curr -= nums[left]
            left += 1
            print(f"left = {left}")
        print(f"ans = {ans}, current length = right {right} - left {left} + 1 = {right - left + 1}")
        ans = max(ans, right - left + 1)
        print(f"ans = {ans}")

    return ans


if __name__ == '__main__':
    print(f"find_length = {find_length([3, 1, 2, 7, 4, 2, 1, 1, 5], 8)}")

    # print("Result = {}".format(pivotIndex([1, 7, 3, 6, 5, 6])))
    # print("Result = {}".format(pivotIndex([1,2,3])))
    # print("Result = {}".format(pivotIndex([-1,-1,-1,-1,-1,0])))
    # print("Result = {}".format(pivotIndex([1, 7, 3, 6, 5, 6])))
    # print(f"Result = {isIsomorphic('egg', 'add')}")
    # print(f"Result = {isIsomorphic('foo', 'bar')}")
    # print(f"Result = {isIsomorphic('paper', 'title')}")
    # print(isSubsequence("abc", "ahbgdc"))
    # print(isSubsequence("axc", "ahbgdc"))
    # a = b = c = [1, 100 , 200]
    # print(f"a = {a}")
    # print(f"b = {b}")
    # print(f"c = {c}")
    # c[0] = 1000
    # print(f"a = {a}")
    # print(f"b = {b}")
    # print(f"c = {c}")
    # b[1] = 2000
    # print(f"a = {a}")
    # print(f"b = {b}")
    # print(f"c = {c}")
    # b = b[1:]
    # print(f"a = {a}")
    # print(f"b = {b}")
    # print(f"c = {c}")
    # c[1] = 400
    # print(f"a = {a}")
    # print(f"b = {b}")
    # print(f"c = {c}")
    # c[2] = 400000
    # print(f"a = {a}")
    # print(f"b = {b}")
    # print(f"c = {c}")

