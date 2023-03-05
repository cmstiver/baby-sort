from baby_sort import CupGame, Stack

cups = CupGame()

cups_list = cups.create_cups(300)
stack = Stack()

cups.baby_sort(cups_list, stack)
