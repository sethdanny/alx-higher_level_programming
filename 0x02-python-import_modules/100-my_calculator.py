#!/usr/bin/python3

def main(argv):
    num = len(argv)
    operators = {
        '+' : calculator_1.add
        '-' : calculator_1.sub
        '*' : calculator_1.mul
        '/' : calculator_1.div

        }
    if num != 4:
       print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
       exit(1)
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

    if operator not in '+-*/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    res = operators[operator](a, b)
    print('{:d} {:s} {:d} = {:d}'.format(a, operator, b, res))

if __name__ == '__main__':
    from calculator_1
    from sys import argv, exit
    main(argv)
