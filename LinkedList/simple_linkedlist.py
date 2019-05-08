'''
Like arrays, Linked List is a linear data structure. Unlike arrays, linked list elements are not stored at contiguous location;
the elements are linked using pointers.

Why Linked List?
Arrays can be used to store linear data of similar types, but arrays have following limitations.
1) The size of the arrays is fixed: So we must know the upper limit on the number of elements in advance. Also, generally, the allocated memory is equal to the upper limit irrespective of the usage.
2) Inserting a new element in an array of elements is expensive, because room has to be created for the new elements and to create room existing elements have to shifted.


For example, in a system if we maintain a sorted list of IDs in an array id[].

id[] = [1000, 1010, 1050, 2000, 2040].

And if we want to insert a new ID 1005, then to maintain the sorted order, we have to move all the elements after 1000 (excluding 1000).
Deletion is also expensive with arrays until unless some special techniques are used. For example, to delete 1010 in id[], everything after 1010 has to be moved.

Advantages over arrays
1) Dynamic size
2) Ease of insertion/deletion
'''


class Node:

    # Function to initialize the node object 
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    # Function to initialize the Linked List object 
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning 
    def push(self,new_data):

        new_node = Node(new_data)

        new_node.next = self.head
    
        self.head = new_node

    # This function is in LinkedList class. Inserts a 
    # new node after the given prev_node. This method is 
    # defined inside LinkedList class shown above */ 
    def insertAfter(self,prev_node,new_data):

        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return
        
        new_node = Node(new_data)

        new_node.next = prev_node.next

        prev_node.next = new_node

    # This function is defined in Linked List class 
    # Appends a new node at the end.  This method is 
    # defined inside LinkedList class shown above */ 
    def append(self,new_data):

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    # Utility function to print the linked list 
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


# Code execution starts here 
if __name__=='__main__': 
  
    # Start with the empty list 
    llist = LinkedList() 
  
    # Insert 6.  So linked list becomes 6->None 
    llist.append(6) 
  
    # Insert 7 at the beginning. So linked list becomes 7->6->None 
    llist.push(7); 
  
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None 
    llist.push(1); 
  
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None 
    llist.append(4) 
  
    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None 
    llist.insertAfter(llist.head.next, 8) 
  
    # print ('Created linked list is:', )
    llist.printList() 