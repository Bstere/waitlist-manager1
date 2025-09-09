# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self, name: str):
        self.name = name      # customer’s name
        self.next = None      # pointer to next node (empty at first)


# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    def __init__(self):
        self.head = None   # start with no customers in the waitlist

    def add_front(self, name):
        new_node = Node(name)        # make a new customer
        new_node.next = self.head    # point it to the old head
        self.head = new_node         # now update head to the new node

    def add_end(self, name):
        new_node = Node(name)
        if self.head is None:
            # if the list is empty, new node becomes the head
            self.head = new_node
            return
        # otherwise, walk to the end of the list
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def remove(self, name):
        if self.head is None:
            print(f"{name} not found")
            return
        # if the head is the one to remove
        if self.head.name == name:
            self.head = self.head.next
            print(f"Removed {name} from the waitlist")
            return
        # otherwise, search for it
        current = self.head
        while current.next is not None:
            if current.next.name == name:
                current.next = current.next.next
                print(f"Removed {name} from the waitlist")
                return
            current = current.next
        print(f"{name} not found")

    def print_list(self):
        if self.head is None:
            print("The waitlist is empty")
            return
        print("Current waitlist:")
        current = self.head
        while current is not None:
            print("-", current.name)
            current = current.next


def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ").strip()
        
        if choice == "1":
            name = input("Enter customer name to add to front: ").strip()
            if name:
                waitlist.add_front(name)
                print(f"Added {name} to the front of the waitlist.")
            else:
                print("Name cannot be empty.")
            
        elif choice == "2":
            name = input("Enter customer name to add to end: ").strip()
            if name:
                waitlist.add_end(name)
                print(f"Added {name} to the end of the waitlist.")
            else:
                print("Name cannot be empty.")
            
        elif choice == "3":
            name = input("Enter customer name to remove: ").strip()
            if name:
                waitlist.remove(name)
            else:
                print("Name cannot be empty.")
            
        elif choice == "4":
            waitlist.print_list()
            
        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")


# Launch the program when the file is run
if __name__ == "__main__":
    waitlist_generator()


"""
Design Memo (≈230 words)

How does your list work?
This tool uses a custom singly linked list to store a sequence of customer names. Each Node holds a customer name and a reference (next) to the following Node. The LinkedList tracks only the head (the first Node). Inserting at the front is O(1) because we make a new Node whose next points to the current head, then update head. Appending to the end is O(n): we traverse until the last node and link the new node there. Removal walks the list to find the target name and relinks the previous node’s next pointer to skip over the removed node. Printing walks from head to tail and prints each name.

What role does the head play?
The head is the entry point (root) of the entire list. If head is None, the waitlist is empty. All operations start from head: adding to the front replaces head, removing the first element updates head, and traversals begin at head to find the tail or a specific name. Keeping head accurate ensures the whole structure remains reachable and consistent.

When might a real engineer need a custom list like this?
Custom lists are useful when you need precise control over memory layout, node content, or insertion/removal costs, and when built-in containers don’t match operational or compliance constraints. Examples include: implementing queues with strict O(1) front insertions; building low-overhead, append-friendly logs; writing embedded systems or high-throughput services with pooled nodes; or crafting specialized structures for schedulers, caches, or networking stacks where pointer-level control, deterministic behavior, or interoperability with C extensions is important.
"""

