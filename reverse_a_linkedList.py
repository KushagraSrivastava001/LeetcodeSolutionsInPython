""

class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        prev=None
        current=head
        while current:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        return prev
