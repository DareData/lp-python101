def fib(element: int):
    if element == 0:
        return 0
    elif element == 1 or element == 2:
        return 1
    else:
        return fib(element-1) + fib(element - 2)

# The following if __name__=='__main__': guarantees that it will only ask me for the input and then
# print the sentence only if I run the script itself. But if other script would call the file, then it
# will load the fib function above the statement without asking for an element
if __name__=='__main__':
    requested_element = int(input("What element in the Fibonacci sequence do you want? "))
    print(f'This is the {requested_element}-th number in the Fibonacci sequence: {fib(requested_element)}')
    