str1 = input("Enter the string to check : " )

str2 = reversed(str1)

if list(str1) == list(str2):
    print(str1+ " is palindrome")
else:
    print(str1+ " is not a palindrome")