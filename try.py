# # # # # # Program to find the ASCII value of the given character

# # # # a='b'
# # # # b='e'
# # # # c = 'p'
# # # # d='S'
# # # # e='G'
# # # # print("The ASCII value of '" + a + "' is", ord(a))
# # # # print("The ASCII value of '" + b + "' is", ord(b))
# # # # print("The ASCII value of '" + c + "' is", ord(c))
# # # # print("The ASCII value of '" + d + "' is", ord(d))
# # # # print("The ASCII value of '" + e + "' is", ord(e))
 
# # # def main():
# # #     # Prompt the user to enter a number
# # #     num = int(input("Enter a number: ",12))

# # #     # Convert the number to hexadecimal and octal formats
# # #     hex_num = hex(num)
# # #     oct_num = oct(num)

# # #     # Display the results
# # #     print("Hexadecimal equivalent:", hex_num)
# # #     print("Octal equivalent:", oct_num)

# # # # if __name__ == "__main__":
# # # #     main()
# # dec=355
# # print(hex(dec), "in hexadecimal.")
# # print(oct(dec), "in octal.")whats
# # Integer variable
# num = 10
# print("Value of num:", num)

# # Float variable
# pi = 3.14
# print("Value of pi:", pi)

# # String variable
# name = "John"
# print("Value of string:", name)

# # Boolean variable
# is_true = True
# print("Value of boolean:", is_true)

# # List variable
# my_list = [1, 2, 3, 4, 5]
# print("Value of list:", my_list)

# # Tuple variable
# my_tuple = (6, 7, 8, 9, 10)
# print("Value of tuple:", my_tuple)

# # Dictionary variable
# my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
# print("Value of dict:", my_dict)
num = int(input("Enter a number: "))

# Convert decimal to hexadecimal
hex_num = hex(num)[2:].upper()
print(f"Hexadecimal equivalent: {hex_num}")

# Convert decimal to octal
oct_num = oct(num)[2:]
print(f"Octal equivalent: {oct_num}")
