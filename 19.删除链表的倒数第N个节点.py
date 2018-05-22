class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        """ version 1
        if head.next == None and n == 1:
            return head
        temp = head
        t = head
        m = n
        while n - 1 > 0:
            n-=1
            temp = temp.next
        if m == 1: # 删除最后一个节点
            while t.next.next != None:
                t = t.next
            t.val = t.next.val
            t.next = None
        else:
            while temp.next != None:
                t = t.next
                temp = temp.next
            t.val = t.next.val
            t.next = t.next.next
        """
        """version 2
        dummy = ListNode()
        dummy.next = head
        sec = dummy
        while n > 0:
            sec = sec.next
            n -= 1
        cur = dummy
        while(sec.next != None):
            sec = sec.next
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next
        """




