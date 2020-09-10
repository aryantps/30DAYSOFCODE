"""
link- https://leetcode.com/problems/design-linked-list/


Statement - Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. 
            A node in a singly linked list should have two attributes: val and next. val is the value of the current node, 
            and next is a pointer/reference to the next node. If you want to use the doubly linked list, 
            you will need one more attribute prev to indicate the previous node in the linked list. 
            Assume all nodes in the linked list are 0-indexed.
            Implement these functions in your linked list class:
                get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
                addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, 
                    the new node will be the first node of the linked list.
                addAtTail(val) : Append a node of value val to the last element of the linked list.
                addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. 
                    If index equals to the length of linked list, the node will be appended to the end of linked list. 
                    If index is greater than the length, the node will not be inserted.
                deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
"""

class Node:
    def __init__(self,val):

        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        ind = 0
        temp = self.head
        while temp != None:
            if ind == index:
                return temp.val
            temp = temp.next
            ind += 1
        return -1


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        avail = Node(val)
        avail.next = self.head
        self.head = avail
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.head is None:
            self.addAtHead(val)
        avail = Node(val)
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = avail
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        avail = Node(val)
        if index==0:
            self.addAtHead(val)
        
        current = self.head
        curr_index = 0

        while current is not None and curr_index < index - 1:
            current = current.next
            curr_index += 1
        if current is None:
            return
        
        avail.next = current.next
        current.next = avail


        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.head is None:
            return
        if index == None:
            current = self.head
            while current.next.next is not None:
                #set the reference of the second last element to none
                current = current.next
            current.next = None
            return
        if index == 0:
            self.head = self.head.next
            return 
        previous = self.head
        for i in range(index-1):
            previous = previous.next
            if previous is None:
                break
        if previous is None or previous.next is None:
            #print('ERROR')
            return 
        previous.next = (previous.next.next)
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)