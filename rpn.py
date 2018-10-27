#!/usr/bin/env python3

def calculate(arg):
    stack = []
    tokens = arg.split()
    for token in tokens:
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            val1 = stack.pop()
            val2 = stack.pop()
            if token == '+':
                result = val1 + val2
            elif token == '-':
                result = val2 - val1
            elif token == '*':
                result = val2 * val1
            elif token == '/':
                result = val2 / val1
            elif token == '^':
                result = val2 ** val1
            stack.append(result)

    if len(stack) > 1:
        raise ValueError('too many arguments on the stack')

    return stack[0]
    pass

def main():
    while True:
        try:
            result = calculate(input('rpn calc> '))
            print(result)
        except ValueError:
            pass

if __name__ == '__main__':
    main()
