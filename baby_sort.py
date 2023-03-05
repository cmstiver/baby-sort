import random


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value


class CupGame:
    @staticmethod
    def create_cups(amount):
        cup_list = list(range(1, amount + 1))
        random.shuffle(cup_list)
        return cup_list
    
    @staticmethod
    def baby_sort(cups_list: list, stack: Stack):
        print(f"Sorting list {cups_list} into a stack.")

        while True:
            top = stack.peek()

            if len(cups_list) > 1:
                index = random.randrange(len(cups_list) - 1)
            elif len(cups_list) == 1:
                index = 0
            else:
                return stack

            cup_size = cups_list[index]
            print(
                f"Attempting to fit cup with the size of {cup_size} into top cup...")
            if top == None:
                print("None.")
            else:
                print(stack)

            if top == None:
                cup = cups_list.pop(index)
                stack.push(cup)
                print(stack)
            elif cup_size < top:
                cup = cups_list.pop(index)
                stack.push(cup)
                print(stack)
            elif cup_size > top:
                print(
                    "\033[1;31;40mRemoving cups from top until this cup fits:\033[0m")
                while top != None and cup_size > top:
                    cup = stack.pop()
                    cups_list.append(cup)
                    top = stack.peek()
                    if top == None:
                        print("\033[1;31;40mNone.\033[0m")
                    else:
                        print(f"\033[1;31;40m{stack}\033[0m")

                cup = cups_list.pop(index)
                stack.push(cup)
                print(stack)
