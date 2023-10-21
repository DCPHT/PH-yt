class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1:
# Time complexity: O(n)
# Space complexity: O(n)
def mergeTwoListsN(list1, list2):
    dummy = ListNode()
    cur = dummy
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = ListNode(list1.val)
            list1 = list1.next
        else:
            cur.next = ListNode(list2.val)
            list2 = list2.next
        cur = cur.next
    if list1:
        cur.next = list1
    if list2:
        cur.next = list2
    return dummy.next


# Solution 2:
# Time complexity: O(n)
# Space complexity: O(1)
def mergeTwoLists(list1, list2):
    dummy = ListNode()
    cur = dummy
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next
    if list1:
        cur.next = list1
    if list2:
        cur.next = list2
    return dummy.next
