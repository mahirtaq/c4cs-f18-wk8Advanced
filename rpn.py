#!/usr/bin/env python3
#skdslfjlkdfj
import readline
import colored, sys
from colored import stylize_interactive, fg
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
            elif token == '%':
                result = val2 % val1
            stack.append(result)
            answer = colored.fg(10) + colored.attr("bold")
            print(val2, stylize_interactive(token, colored.fg(164)), val1, '=', stylize_interactive(result, answer))

    if len(stack) > 1:
        raise ValueError('too many arguments on the stack')
    pass

def main():
    while True:
        try:
            calculate(input('rpn calc> '))
        except ValueError:
            pass

if __name__ == '__main__':
    main()
