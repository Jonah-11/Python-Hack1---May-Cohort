#1. Reverse a String Using a Stack
#Implement a stack data structure to reverse a string.

def reverse_string(s: str) -> str:
    stack = []
    
    # Push each character onto the stack
    for char in s:
        stack.append(char)
    
    # Pop characters from the stack to get them in reverse order
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

# Example usage
user = input("Enter a word: ")
print("The reverse of your word is: ", reverse_string(user))  # Output: "olleh"

#2. Implement a Queue Using Two Stacks
class QueueWithStacks:
    def __init__(self):
        self.stack_in = []  # Stack to handle enqueue operations
        self.stack_out = [] # Stack to handle dequeue operations

    def enqueue(self, x: int):
        self.stack_in.append(x)

    def dequeue(self) -> int:
        if not self.stack_out:  # Transfer elements if stack_out is empty
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if self.stack_out:  # Check again to handle empty queue cases
            return self.stack_out.pop()
        raise IndexError("Dequeue from an empty queue")

# Example usage
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2

#Find the Maximum Element in a List Using a Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: int):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def find_max(self) -> int:
        if not self.head:
            raise ValueError("List is empty")
        max_value = self.head.data
        current = self.head.next
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        return max_value

# Example usage
b = LinkedList()
b.append(3)
b.append(1)
b.append(4)
b.append(2)
print("The largest number is ", b.find_max())  # Output: 4
