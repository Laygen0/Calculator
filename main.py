def get_formula(src):
    dst = []
    number = ''

    for i in range(len(src)):

        if src[i] in '1234567890.':
            number += src[i]
        elif src[i] == ' ':
            pass
        else:
            if number: dst.append(float(number))
            number = ''
            dst.append(src[i])

        if i == len(src) - 1:
            if number: dst.append(float(number))
            number = ''

    return dst

def get_rpn(dst, stack):
    rpn = []

    for elem in dst:

        if elem in operators:
            while stack and stack[-1] != '(' and operators[elem][0] >= operators[stack[-1]][0]:
                rpn.append(stack.pop())
            stack.append(elem)

        elif elem == ')':
            while stack:
                a = stack.pop()
                if a == '(':
                    break
                rpn.append(a)

        elif elem == '(':
            stack.append(elem)

        else:
            rpn.append(elem)

    while stack:
        rpn.append(stack.pop())

    return rpn


operators = {'*': (1, lambda x, y: x * y),
             '/': (1, lambda x, y: x / y),
             '+': (2, lambda x, y: x + y),
             '-': (2, lambda x, y: x - y),}

formula_src = input('Введите выражение: ')
formula_dst = get_formula(formula_src)
stack = []
rpn = get_rpn(formula_dst, stack)

for elem in rpn:

    if elem in operators:
        y, x = stack.pop(), stack.pop()
        stack.append(operators[elem][1](x,y))

    else: stack.append(elem)

print(f'Ответ: {stack[0]}')