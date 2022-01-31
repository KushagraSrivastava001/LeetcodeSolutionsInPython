class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        # remove the loop without losing any nodes
        s=set()
        prev=None
        while head:
            if head in s:
                prev.next=None
                return True
            else:
                s.add(head)
                prev=head
                head=head.next
        return False
