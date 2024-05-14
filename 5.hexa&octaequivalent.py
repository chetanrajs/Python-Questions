num=int(input("Enter a number:"))
hex_num=hex(num)[2:].upper()
print(f"Hexadecimal equivalent:{hex_num}")
oct_num=oct(num)[2:]
print(f"Octal equivalent:{oct_num}")