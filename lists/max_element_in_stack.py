"""
You have an empty sequence, and you will be given  queries. Each query is one of these three types:

1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.

------------
Input Format
------------
The first line of input contains an integer, N.
The next N lines each contain an above mentioned query.

*****
TASK
*****
For each type  query, print the maximum element in the stack on a new line.

"""

stack = []
n = int(raw_input())
for queries in xrange(n):
    q_set = raw_input()
    if len(q_set) > 1:
        q_type, q_val = map(int, q_set.split())
    else:
        q_type = int(q_set)

    if q_type == 1:
        stack.append(q_val)
    elif len(stack) == 0:
        continue
    elif q_type == 2:
        stack.pop()
    else:
        print max(stack)
