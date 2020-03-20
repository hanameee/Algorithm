N = int(input())
for i in range(N):
    commands = input()
    left_stack = list()
    right_stack = list()
    for command in commands:
        if command == '-':
            if left_stack:
                left_stack.pop()
        elif command == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif command == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(command)
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))
