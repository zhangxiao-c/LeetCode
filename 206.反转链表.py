# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        if head.next == None:
            return head
        fir = head
        sec = head.next
        head.next = None
        while sec != None:
            temp = sec.next
            sec.next = fir
            fir = sec
            sec = temp
        return fir
        """version 2
        pre = head
        p = head.next
        pre.next = None
        while p != None:
            temp = p.next
            p.next = pre
            pre = p
            p = temp
        return pre
        """