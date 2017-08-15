import stack

stack = stack.Stack()
for c in 'Hello':
    stack.push(c)

reverse = ''

for i in range(len(stack.items)):
    reverse += stack.pop()

print(reverse)
