#from stack import Stack
import stack

myWord = input('Type any word here: \n')

stack1 = stack.Stack()
for c in myWord:
    stack1.push(c)

reverse = ''

for i in range(len(stack1.items)):
    reverse += stack1.pop()

print(reverse)

list1 = [1, 2, 3, 4, 5]
list2 = []

stack2 = stack.Stack()
for i in list1:
    stack2.push(i)

for item in range(len(stack2.items)):
    list2.append(stack2.pop())

print(list2)


