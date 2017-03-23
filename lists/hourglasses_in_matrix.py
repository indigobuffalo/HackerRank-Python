"""
Given a 6 X 6 2D Array, A:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

we define an hourglass in A to be a subset of values with indices in this pattern:

a b c
  d
e f g

There are  hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

******
TASK:
******

Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

-------------
Input Format
-------------

There are 6 lines of input, where each line contains 6 space-separated integers describing 2D Array A;
every value in A will be in the inclusive range of -9 to 9.

~~~~~~~~~~~~
Constraints
~~~~~~~~~~~~

   -9 <= A[i][j] <= 9

    0 <= i,j <= 5


"""
arr = []
for arr_i in xrange(6):
    arr_temp = map(int, raw_input().strip().split(' '))
    arr.append(arr_temp)

h_gs = []
for i, j in [(i, j) for i in xrange(4) for j in xrange(4)]:
    h_g = [arr[i][j], arr[i][j+1], arr[i][j+2],
           arr[i+1][j+1],
           arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2]]
    h_gs.append(h_g)

sums = [sum(x) for x in h_gs]
print max(sums)

