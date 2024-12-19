'''n=int(input()) #take input between 1,20 and print the square upto that number 
if 1<n<20:

    for i in range(n):
        print(i*i)
else:
    print("Not possible")'''

 
""" The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .

Example

The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

0
1
4
Input Format

The first and only line contains the integer, .

Constraints


Output Format

Print  lines, one corresponding to each .

Sample Input 0

5
Sample Output 0

0
1
4
9
16"""   
            

# Input a number from the user
num = int(input("Enter a number: "))

# Check if the number is even
if num % 2 == 0:
    print(f"{num} is an even number.")
    print("Even numbers between 2 and", num, ":")
    for i in range(2, num + 1, 2):  # Increment by 2 to get even numbers
        print(i, end=" ")
else:
    print(f"{num} is not an even number.")

