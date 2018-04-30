
stack = []


while True:
    inp = input("i/o")
    if inp == "i":
        stack.append(int(input("data")))
    elif inp == "o":
        print(stack.pop())
    print(stack)
    # bnm
