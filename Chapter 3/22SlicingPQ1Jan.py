"""Slicing  Practice Question : 
Write a program that takes your favorite food name as input and prints: 
● The middle 3 characters 
 
● The last 2 characters""" 
Str1 = input("Enter your favorite food name: ")

# Length of the string
fc = len(Str1)

# Middle 3 characters
mid = fc // 2   # index of the middle character
print("Middle 3 characters:", Str1[mid-1:mid+2])

# Last 2 characters
print("Last 2 characters:", Str1[-2:])
